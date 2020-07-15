HorarioMatriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]



TerminarProceso = 0

while TerminarProceso < 1:
  #Intro
  print (" ")
  print ("Bienvenido a la pagina de reservación de visitas guiadas por la UTEC")
  print (" ")

  print ("Horario de atención:")
  print ("Lunes - Viernes")
  print ("8:00 AM - 6:00 PM")
  print (" ")

  print ("Todas las visitas guiadas tienen una duración de 2 horas")
  print (" ")

  #Nombre
  InputNombre = str(input("Para empezar ingrese su nombre: "))
  print (" ")

  EmailUsuario = input("Ingrese su correo electronico: ")
  print (" ")

  Telefono = input("Ingrese su número telefónico: ")
  print (" ")
  #Fecha
  FechaMatriz = 0
  InputFecha = str(input("Para que día desearía hacer su reserva: "))
  InputFecha = InputFecha.lower()

  #Entregador de numero del 0 al 4 por fecha
  if InputFecha == "lunes":
    FechaMatriz = 0
  elif InputFecha == "martes":
    FechaMatriz = 1
  elif InputFecha == "miercoles":
    FechaMatriz = 2
  elif InputFecha == "jueves":
    FechaMatriz = 3
  elif InputFecha == "viernes":
    FechaMatriz = 4
  else:
    #En caso de datos no validos
    print (" ")
    print("ERROR")
    print("DATOS NO VALIDOS")
    print ("POR FAVOR REINICIE EL PROGRAMA")
    sys.exit(1)
  print (" ")


  #Entregador de numero del 0 al 4 por hora (Unico formato aceptado : hh:mm)
  HoraMatriz = 0
  print("¿Para que horario desearía hacer su reserva? ")
  print("Los horarios son:")
  print("8:00 - 10:00")
  print("10:00 - 12:00")
  print("12:00 - 14:00")
  print("14:00 - 16:00")
  print("16:00 - 18:00")
  print (" ")

  InputHora = input("Horario: ")
  NumeroHora = 0

  if InputHora == "8:00 - 10:00":
    NumeroHora = 0
  elif InputHora == "10:00 - 12:00":
    NumeroHora = 1
  elif InputHora == "12:00 - 14:00":
    NumeroHora = 2
  elif InputHora == "14:00 - 16:00":
    NumeroHora = 3
  elif InputHora == "16:00 - 18:00":
    NumeroHora = 4
  
  ArchivoCitas = open('citas.txt', "a")
  ArchivoCitas.write('---\n')
  ArchivoCitas.write('Nombre: ' + InputNombre.upper() + '\n')
  ArchivoCitas.write('Email: ' + EmailUsuario + '\n')
  ArchivoCitas.write('Número Telefónico: ' + Telefono + '\n')
  ArchivoCitas.write('Día: ' + InputFecha.upper() + '\n')
  ArchivoCitas.write('Hora: ' + InputHora + '\n')
  ArchivoCitas.write(' \n')
  ArchivoCitas.close()

  CambioMatriz = []
  Verificador1 = HorarioMatriz[FechaMatriz]

  def Exitosa(h):
    print ("¡Reservación exitosa!")
    print ("Datos de la reservación:")
    print ("Nombre: ", InputNombre.upper())
    print ("Día:", InputFecha.upper())
    print ("Hora:", h)
    


  if Verificador1[NumeroHora] == 0:
    if InputHora == "8:00 - 10:00":
      CambioMatriz = HorarioMatriz [FechaMatriz]
      CambioMatriz[0] = InputNombre
      HorarioMatriz[FechaMatriz] = CambioMatriz
      CambioMatriz = []
      Exitosa(InputHora)
    elif InputHora == "10:00 - 12:00":
      CambioMatriz = HorarioMatriz [FechaMatriz]
      CambioMatriz[1] = InputNombre
      HorarioMatriz[FechaMatriz] = CambioMatriz
      CambioMatriz = []
      Exitosa(InputHora)
    elif InputHora == "12:00 - 14:00":
      CambioMatriz = HorarioMatriz [FechaMatriz]
      CambioMatriz[2] = InputNombre
      HorarioMatriz[FechaMatriz] = CambioMatriz
      CambioMatriz = []
      Exitosa(InputHora)
    elif InputHora == "14:00 - 16:00":
      CambioMatriz = HorarioMatriz [FechaMatriz]
      CambioMatriz[3] = InputNombre
      HorarioMatriz[FechaMatriz] = CambioMatriz
      CambioMatriz = []
      Exitosa(InputHora)
    elif InputHora == "16:00 - 18:00":
      CambioMatriz = HorarioMatriz [FechaMatriz]
      CambioMatriz[4] = InputNombre
      HorarioMatriz[FechaMatriz] = CambioMatriz
      CambioMatriz = []
      Exitosa(InputHora)
    else:
      #En caso de datos no validos
      print (" ")
      print("ERROR")
      print("SU ELECCIÓN NO SE ENCUENTRA EN LAS OPCIONES BRINDADAS")
      print ("POR FAVOR REINICIE EL PROGRAMA")
      sys.exit(1)
  else: 
    print ("Este horario ya ha sido tomado")
  print (" ")
  
  print ("¿Desea hacer otra reserva?")
  print ("(Si - No)")
  Continuar = str(input(" "))
  Continuar = Continuar.upper()
  Afirmativo = "SI"
  if Continuar == Afirmativo:
    TerminarProceso = 0
  else:
    TerminarProceso = 2

print("Muchas Gracias!")
print("En caso tenga dudas o consultas comuniquese al (01) 3173900")
