import hashlib
#hashlib={}
#class Person(object):
invalid=True
#def __init__(self, name=None, bname=None, isbn=None, d={},) :
 #          self.name = name
  #         self.job = job
   #        self.quote = quote
           #self.hash = hash
    #       d.book = book
#create an empty list
personList = [[],[],[],[],[]]
#Creating more Lists will be best but keeping just one might also work.
edit=0
menu=0
def load():
    print "Welcome to the library"
    print "1-add book"
    print "2-edit book"
    print "3-delete book"
    print "4-show all books"
    print "5-Search for Id"
    print "6-search for Book name"
    print "7-search for ISBN"
    print "8-log out"
    menu=int(raw_input("select a number from 1 to 6: "))
    
    
    if menu==1:
        print "1-Agregar 1er Libro: "
        print "2-Agregar 2do Libro: "
        print "3-Agregar 3er Libro: "
        print "4-Agregar 4to Libro: "
        print "5-Agregar 5to Libro: "
        sec=int(raw_input("En caul seccion quieres guardar tu libro: "))
        if sec==1:
          idc=raw_input("book id: ")
          Arthor=raw_input("nombre de Autor: ")
          book=raw_input("nombre del libro: ")
          ed=raw_input("Edicion: ")
          isb=raw_input("ISBN: ")
          date=raw_input("Fecha: ")
          city=raw_input("ciudad: ")
          com=raw_input("Comment: \n")
          personList[0].extend((idc, Arthor,book,ed,isb,date,city,com))
          invalid=False
        elif sec==2:
          idc=raw_input("book id: ")
          Arthor=raw_input("nombre de Autor: ")
          book=raw_input("nombre del libro: ")
          ed=raw_input("Edicion: ")
          isb=raw_input("ISBN: ")
          date=raw_input("Fecha: ")
          city=raw_input("ciudad: ")
          com=raw_input("Comment: \n")
          personList[1].extend((idc, Arthor,book,ed,isb,date,city,com))
          invalid=False
        elif sec==3:
          idc=raw_input("book id: ")
          Arthor=raw_input("nombre de Autor: ")
          book=raw_input("nombre del libro: ")
          ed=raw_input("Edicion: ")
          isb=raw_input("ISBN: ")
          date=raw_input("Fecha: ")
          city=raw_input("ciudad: ")
          com=raw_input("Comment: \n")
          personList[2].extend((idc, Arthor,book,ed,isb,date,city,com))
          invalid=False
        elif sec==4:
          idc=raw_input("book id: ")
          Arthor=raw_input("nombre de Autor: ")
          book=raw_input("nombre del libro: ")
          ed=raw_input("Edicion: ")
          isb=raw_input("ISBN: ")
          date=raw_input("Fecha: ")
          city=raw_input("ciudad: ")
          com=raw_input("Comment: \n")
          personList[3].extend((idc, Arthor,book,ed,isb,date,city,com))
          invalid=False
        elif sec==4:
          idc=raw_input("book id: ")
          Arthor=raw_input("nombre de Autor: ")
          book=raw_input("nombre del libro: ")
          ed=raw_input("Edicion: ")
          isb=raw_input("ISBN: ")
          date=raw_input("Fecha: ")
          city=raw_input("ciudad: ")
          com=raw_input("Comment: \n")
          personList[4].extend((idc, Arthor,book,ed,isb,date,city,com))
          invalid=False
            
    elif menu == 4:
        if personList==[]:
            print "No data"
            invalid=False
        else:
                
        
            #d[frozenset(personList)] = 0
            # print dictionary of first class instance
            print "ID: "
            print (personList[0][0])
              #{'person0': 0, 'person1': 1}
                # print dictionary of second class instance
            print "Arthor: "    
            print (personList[0][1])
              #{'person0': 0, 'person1': 1}
            print "Book name: "
            print (personList[0][2])
              #{'person0': 0, 'person1': 1}
            print "Edition:"
            print (personList[0][3])
              #{'person0': 0, 'person1': 1}
            print "ISBN:"
            print (personList[0][4])
              #{'person0': 0, 'person1': 1}
            print "Fecha:"
            print (personList[0][5])
              #{'person0': 0, 'person1': 1}
            print "ciudad:"
            print (personList[0][6])
              #{'person0': 0, 'person1': 1}
            print "Comment:"
            print (personList[0][7])
              #{'person0': 0, 'person1': 1}
            
    elif menu == 2:
        print "OPCIONES:\n"
        print "1-Edit id"
        print "2-Edita Autor"
        print "3-Editar Nombre"
        print "4-Edit Edicion"
        print "5-Edit ISBN"
        print "6-Edit Fecha"
        print "7-Edit Ciudad"
        print "8-Edit Comentario"
        print "9-Exit"
        edit=int(raw_input("Selecione un numero de las opciones: "))
        if edit == 1:
            print "hello"
            we=raw_input("Nuevo Id: ")
            personList[0]=we
            print "Nuevo ID: "+ personList[0]
        elif edit==2:
            we=raw_input("Nuevo Autor: ")
            personList[1]=we
            print "Nuevo Autor: "+personList[1]
        elif edit==3:
            we=raw_input("Nuevo Nombre: ")
            personList[2]=we
        elif edit == 4:
            we=raw_input("Nueva Edicion: ")
            personList[3]=we
        elif edit == 5:
            we=raw_input("Nueva ISBN: ")
            personList[4]=we
        elif edit == 6:
            we=raw_input("Nueva Fecah: ")
            personList[5]=we
        elif edit == 7:
            we=raw_input("Nueva Ciudad: ")
            personList[6]=we
        elif edit == 8:
            we=raw_input("Nuevo Comentario: ")
            personList[7]=we
            
        else:
            print "bye"
    else:
        print "bye"
        
while invalid:
    load()
raw_input()
