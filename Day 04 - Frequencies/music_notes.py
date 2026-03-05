def dompier_music(switches):
  # Write code below 💖
  frequency_to_note ={
    261	: "C4",
    294	: "D4",
    329	: "E4",
    349	: "F4",
    392	: "G4",
    440	: "A4",
    494	: "B4",
    523	: "C5",
    0	: "REST"
  }

  result = []

  for switch in switches:
    decimal = int(switch, 2)
    note = frequency_to_note[decimal]
    result.append(note)

  return result