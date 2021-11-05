def add_time(start, duration, dias_da_semana=False):

  start_tuple = start.partition(":")
  start_minutos_tuple = start_tuple[2].partition(" ")
  start_horas = int(start_tuple[0])
  start_minutos = int(start_minutos_tuple[0])
  am_or_pm = start_minutos_tuple[2]
  am_e_pm_flip = {"AM": "PM", "PM": "AM"}

  duration_tuple = duration.partition(":")
  duration_horas = int(duration_tuple[0])
  duration_minutos = int(duration_tuple[2])

  dias_da_semana_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  dias_da_semana_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  quantidade_dias = (duration_horas // 24)

  minutos_final = start_minutos + duration_minutos
  if(minutos_final >= 60):
    start_horas += 1
    minutos_final = minutos_final % 60
  amount_of_am_pm_flips = (start_horas + duration_horas) // 12
  end_horas = int(start_horas + duration_horas) % 12

  minutos_final = minutos_final if minutos_final > 9 else "0" + str(minutos_final)
  end_horas = end_horas = 12 if end_horas == 0 else end_horas
  if(am_or_pm == "PM" and start_horas + (duration_horas % 12) >= 12):
    quantidade_dias += 1

  am_or_pm = am_e_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm
  
  novo_tempo = str(end_horas) + ":" + str(minutos_final) + " " + am_or_pm
  if(dias_da_semana):
    dias_da_semana = dias_da_semana.lower()
    index = int((dias_da_semana_index[dias_da_semana]) + quantidade_dias) % 7
    novo_dia_da_semana = dias_da_semana_array[index]
    novo_tempo += ", " + novo_dia_da_semana

  if(quantidade_dias == 1):
    return novo_tempo + " " + "(next day)"
  elif(quantidade_dias > 1):
    return novo_tempo + " (" + str(quantidade_dias) + " days later)"

  return novo_tempo