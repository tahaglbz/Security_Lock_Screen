import tkinter as tk
from tkinter import messagebox
import keyboard
import cv2
import threading
import time
import sys
import pygame  

class LockScreen:
    def __init__(self, password="1234", timer=30):
        self.password = password
        self.timer = timer
        self.is_authenticated = False
        self.video_recording = False
        self.is_gui_initialized = False

        pygame.mixer.init()

    def initGUI(self):
        self.root = tk.Tk()
        self.root.title("Kilit Ekranı")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.focus_force()
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.block_keys()

        self.setup_ui()

        self.keep_on_top()

        self.start_timer()
        self.is_gui_initialized = True

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(expand=True, fill='both')

        title_label = tk.Label(
            main_frame,
            text="Kilit Ekranı",
            font=('Arial', 24, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=50)

        password_frame = tk.Frame(main_frame, bg='#2c3e50')
        password_frame.pack(pady=20)

        password_label = tk.Label(
            password_frame,
            text="Şifre:",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='white'
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            password_frame,
            font=('Arial', 16),
            show="*",
            width=20
        )
        self.password_entry.pack(pady=10)

        login_button = tk.Button(
            main_frame,
            text="Kilidi Aç",
            command=self.check_password,
            font=('Arial', 14),
            bg='#3498db',
            fg='white',
            width=15
        )
        login_button.pack(pady=10)

        self.password_entry.bind('<Return>', lambda e: self.check_password())

        self.timer_label = tk.Label(
            main_frame,
            text=f"Kalan Süre: {self.timer} saniye",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='white'
        )
        self.timer_label.pack(pady=10)

        self.password_entry.focus_force()

    def start_timer(self):
        def countdown():
            while self.timer > 0:
                if self.is_authenticated:
                    break
                time.sleep(1)
                self.timer -= 1
                self.update_timer_label()

            if not self.is_authenticated:
                self.trigger_alarm()

        threading.Thread(target=countdown, daemon=True).start()

    def update_timer_label(self):
        self.timer_label.config(text=f"Kalan Süre: {self.timer} saniye")

    def trigger_alarm(self):
        self.play_alarm_sound()  
        self.start_video_recording()

    def play_alarm_sound(self):
        try:
            pygame.mixer.music.load('alarm.wav')
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Hata", f"Alarm sesi çalarken bir hata oluştu: {e}")

    def start_video_recording(self):
        self.video_recording = True
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Hata", "Kamera açılamadı!")
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        def display_video():
            start_time = time.time()
            while self.video_recording and time.time() - start_time < 10:
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                    cv2.imshow('Recording', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()
            self.video_recording = False

        threading.Thread(target=display_video, daemon=True).start()

    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == self.password:
            self.is_authenticated = True
            self.unblock_keys()
            self.root.destroy()
            sys.exit()
        else:
            messagebox.showerror("Hata", "Yanlış şifre!")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_force()

    def disable_event(self, event=None):
        self.root.focus_force()
        self.password_entry.focus_force()
        return "break"

    def block_keys(self):
        def block_key_event(e):
            return False

        keyboard.hook_key('tab', block_key_event, suppress=True)
        keyboard.hook_key('alt', block_key_event, suppress=True)
        keyboard.hook_key('left windows', block_key_event, suppress=True)
        keyboard.hook_key('right windows', block_key_event, suppress=True)
        keyboard.hook_key('delete', block_key_event, suppress=True)
        keyboard.hook_key('esc', block_key_event, suppress=True)
        keyboard.hook_key('ctrl', block_key_event, suppress=True)
        keyboard.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
        keyboard.add_hotkey('ctrl+alt+delete', lambda: None, suppress=True)
        keyboard.add_hotkey('alt+f4', lambda: None, suppress=True)
        keyboard.add_hotkey('alt+tab', lambda: None, suppress=True)

    def unblock_keys(self):
        keyboard.unhook_all()
        keyboard.remove_all_hotkeys()

    def keep_on_top(self):
        self.root.lift()
        self.root.focus_force()
        self.password_entry.focus_force()
        self.root.after(100, self.keep_on_top)

    def run(self):
        if not self.is_gui_initialized:
            self.initGUI()
        try:
            self.root.mainloop()
        except:
            self.unblock_keys()
            sys.exit()
        finally:
            self.unblock_keys()

if __name__ == "__main__":
    try:
        keyboard.hook_key('windows', lambda e: False, suppress=True)
    except Exception as e:
        messagebox.showerror("Hata", "Bu program admin haklarıyla çalıştırılmalıdır!")
        sys.exit()

    lock_screen = LockScreen(password="1234")
    lock_screen.run()
