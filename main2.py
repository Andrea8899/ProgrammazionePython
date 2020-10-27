# tutti gli import necessari per l'applicazione
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.operatore = ""
        
        """Questo è il boxlayout dove verrà contenuto il widget 
        label che a sua volta verrà visualizzato il risultato 
        dell'operazione"""

        self.output_box = BoxLayout(orientation="vertical")
        self.output_lb = Label(text ="", font_size=50)
        self.output_box.add_widget(self.output_lb)
        
        """Questo è il gridlayout dove verranno
        contenuti i tasti numerici e gli operatori """
        
        self.input_grid = GridLayout(cols = 4 )
        """ Pulsanti numerici"""
        self.btn_1 = Button(text = "1")
        self.btn_1.bind(on_press=self.uno)
        self.btn_2 = Button(text = "2")
        self.btn_2.bind(on_press=self.due)
        self.btn_3 = Button(text = "3")
        self.btn_3.bind(on_press=self.tre)
        self.btn_4 = Button(text = "4")
        self.btn_4.bind(on_press=self.quattro)
        self.btn_5 = Button(text = "5")
        self.btn_5.bind(on_press=self.cinque)
        self.btn_6 = Button(text = "6")
        self.btn_6.bind(on_press=self.sei)
        self.btn_7 = Button(text = "7")
        self.btn_7.bind(on_press=self.sette)
        self.btn_8 = Button(text = "8")
        self.btn_8.bind(on_press=self.otto)
        self.btn_9 = Button(text = "9")
        self.btn_9.bind(on_press=self.nove)
        self.btn_zero = Button(text = "0")
        self.btn_zero.bind(on_press=self.zero)

        """Pulsanti Operatori"""
        self.btn_piu = Button(text = "+")
        self.btn_piu.bind(on_press=self.memorizza)
        self.btn_meno = Button(text = "-")
        self.btn_meno.bind(on_press=self.memorizza)
        self.btn_per= Button(text = "x")
        self.btn_per.bind(on_press=self.memorizza)
        self.btn_diviso = Button(text = ":")
        self.btn_diviso.bind(on_press=self.memorizza)
        self.btn_uguale = Button(text = "=")
        self.btn_uguale.bind(on_press=self.risultato)
        self.btn_cancellare = Button(text = "C")
        self.btn_cancellare.bind(on_press=self.cancella)
        


        self.input_grid.add_widget(self.btn_1)
        self.input_grid.add_widget(self.btn_2)
        self.input_grid.add_widget(self.btn_3)
        self.input_grid.add_widget(self.btn_cancellare)
        self.input_grid.add_widget(self.btn_4)
        self.input_grid.add_widget(self.btn_5)
        self.input_grid.add_widget(self.btn_6)        
        self.input_grid.add_widget(self.btn_meno)
        self.input_grid.add_widget(self.btn_7)
        self.input_grid.add_widget(self.btn_8)
        self.input_grid.add_widget(self.btn_9)
        self.input_grid.add_widget(self.btn_diviso)
        self.input_grid.add_widget(self.btn_per) 
        self.input_grid.add_widget(self.btn_zero)   
           
        """ Pulsante risultato e cancellazione"""
        
        self.input_grid.add_widget(self.btn_uguale)
        self.input_grid.add_widget(self.btn_piu)
        
        """Queste righe servono per aggiungere alla classe principale 
        i due layout fondamentali, output_box & input_grid"""
        
        self.add_widget(self.output_box)
        self.add_widget(self.input_grid)
        
    def uno(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_1.text
    def due(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_2.text
    def tre(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_3.text
    def quattro(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_4.text
    def cinque(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_5.text
    def sei(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_6.text
    def sette(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_7.text
    def otto(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_8.text
    def nove(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_9.text
    def zero(self, value):
        self.output_lb.text = self.output_lb.text + self.btn_zero.text

    def memorizza(self, value):
        self.contenitore = []
        self.contenitore.append(self.output_lb.text)
        self.operatore = value.text
        


        self.output_lb.text = ""

    def cancella(self, value):
        self.output_lb.text = ""
    
    def risultato(self,value):
        #valore = 0
        #self.contenitore.append(self.output_lb.text)
        valore = int(self.output_lb.text)
        for i in self.contenitore:
            if self.operatore == "+":
                valore = int(i) +  valore         
            elif self.operatore == "-":
                valore = int(i) - valore           
            elif self.operatore == ":":
                if valore == 0:
                    valore = 1
                valore = int(int(i) / valore)
            else:
                if valore == 0:
                    valore = 1
                valore = int(i) * valore    
          
        self.output_lb.text = str(valore)

class MainApp(App):
    def build(self):
        return Main()

if __name__ == "__main__":
    MainApp().run()


# git clone https://github.com/kivy/buildozer.git
# cd buildozer
# sudo python setup.py install