class Player:
    def action(self):
        print("Аудио файлдарды ойнатуда.")
class Recorder:
    def action(self):
        print("Жаңа аудио материалдарды жазып алуда.")
class MultiMediaDevice(Player, Recorder):
    def action(self):
        super().action()
        print("Сонымен қатар, басқа құрылғылармен синхрондауды басқаруда.")

device = MultiMediaDevice()
print("--- Мультимедиялық Құрылғының Әрекеттері ---")
device.action()