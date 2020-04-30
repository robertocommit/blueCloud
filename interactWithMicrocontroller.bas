
$regfile = "m88def.dat"
$crystal = 8000000
$baud = 76800

'Disable Spi

Config Pinc.0 = Input                                       'configuro ingr adc
Config Pinb.1 = Output                                      'configuro l'out
Config Pinb.0 = Output
Config Pinb.2 = Output

dim Z As String * 10
Dim Cic As Integer
Dim Otre As Integer
Dim Temp As Single
Dim Comando As String * 1
Config Adc = Single , Prescaler = Auto
Start Adc

Config Lcdpin = Pin , Db4 = Portc.4 , Db5 = Portc.5 , Db6 = Portd.6 , Db7 = Portd.7 , E = Portb.4 , Rs = Portb.3
Config Lcd = 20 * 2


Do
  Cic = Cic + 1
  Otre = Getadc(0)
  Waitms 100
  Cls
  Upperline

  Temp = Otre / 14
  Z = Fusing(temp , "#.##")
  Lcd "Val: " ; Z ; "  " ; Cic

  Comando = Inkey()

  Upperline
  Lcd Comando
  Waitms 50
  If Comando = "A" Then Set Portb.0
  If Comando = "A" Then Set Portb.1
  If Comando = "A" Then Set Portb.2
  If Comando = "a" Then Reset Portb.0
  If Comando = "a" Then Reset Portb.1
  If Comando = "a" Then Reset Portb.2:
  Print Z
  Waitms 10
  Loop
End
