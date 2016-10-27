import aiml

# Create a kernel and learn aiml files

kernal = aiml.Kernal()
kernal.learn("stf-startup.xml")
kernal.respond("Load aiml b")


# Ctrl- C to break this loop
while True:
    print (kernal.respond(input("Enter your message >>")))