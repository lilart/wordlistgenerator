import string, random, sys

def generate_characters():
       characters = []
       lower = string.ascii_lowercase
       upper = string.ascii_uppercase
       digit = string.digits

       for i in lower:
              characters.append(i)
       for i in upper:
              characters.append(i)
       for i in digit:
              characters.append(i)
       return characters
              
def generate_password(character_number, characters):
       generated = ""
       for i in range(character_number):
                generated += characters[random.randint(0,len(characters)-1)]
       return generated

if __name__ == '__main__':
       try:
              character_number = int(sys.argv[1])
              output_file = sys.argv[2]
       except:
              print("Python3 {} <NUMBER OF CHARACTERS> <OUTPUT FILE>".format(sys.argv[0]))
              exit()

       x=0
       f = open(output_file, "w+")
       characters = generate_characters()

       try:
              while True:
                     x+=1
                     print("\rPaswords generated: "+ str(x), end="\r")
                     f.write(generate_password(character_number, characters)+"\n")
       except (KeyboardInterrupt, SystemExit):
              print("\nLol")
              f.close()
