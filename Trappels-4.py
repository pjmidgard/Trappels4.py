from time import time 
Circles_functions= 0
import os
import binascii
self="'"



namez = input("for compression c or e for extract: ")

#@Author Jurijus pacalovas

class encypthion_class:



    def encypthion1(self):




                long3=0

                self.name = "Author: Jurijus Pacalovas"



                print(self.name)



                if namez!="c" and namez!="e":

                    print("Your enter incorrect letter")

                

                if namez=="c":
                  

                    name = input("What is name of file? ")

                    if os.path.exists(name):

                            print('Path is exists!')

                    else:

                            print('Path is not exists!')

                            raise SystemExit

                    namea=""

                    namem=""

                    namema="?"

                    Circle155=0

                    Calculusadd=""

                                             

                    Combination=-1

                    Combination1=-1      

                    Times55=0                                

                    Times56=0  

                    Times_of_compressionression_2 =0

                    

                    nameas=name

                    nac=len(nameas)



                    long=len(name)

                   

                    name_cut=len(".bin")

                    

                    nameas=name+".bin"

                    name_bofore=len(nameas)

                    nac=len(nameas)

                    

                    countraz=0
		

                    Circles_functions=2

                    Circles_functions1=0

                    s=""

                    

                 

                    INFO3=""

                    INFO2=""

                

                    



                    ssCircles_functions=0

                    

                    qTimes_compressionCirclesionzl=0



                    block=1



                    x=0

                    x1=0

                    x2=0

                    x = time()



                    with open(nameas, "w") as f4:

                            f4.write(s)

                    with open(nameas, "a") as f3:

                            f3.write(s)

                    with open(name, "rb") as binary_file:



                       # Read the whole file at once

                        data = binary_file.read()

                        

                

                        size_after2=len(data)

                        #print(size_after2)  

                        

                        if len(data)==0 or len(data)>2**40:

                            x4=0.0

                            print(x4)

                            raise SystemExit

                        s=str(data)

                        lenf1=len(data)

                           

                        lenf5=len(data)

                        

                        Times_2=0

                        Times_compressionCirclesionz=0

                       

                        while Times_2<10:


                            Circles_functions=Circles_functions+1

                            

                            countraz=countraz+1



                            with open(nameas, "ab") as f2:

                                if countraz==1:

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    lenf=len(INFO)

                                    lenf1=len(data)

                                

                                    xc=(lenf1*8)-lenf

                                    z=0

                                    if xc!=0:

                                        while z<xc:

                                            INFO="0"+INFO

                                            z=z+1

                                    if countraz==1:

                                        INFO2=INFO

                            

                                    n = int(INFO2, 2)

                                

                                    binary_to_data=len(INFO2)

                                    binary_to_data=(binary_to_data/8)*2

                                    binary_to_data=str(binary_to_data)

                                    binary_to_data="%0"+binary_to_data+"x"

                             

                                    jl=binascii.unhexlify(binary_to_data % n)

                                    long6=len(jl)

                                    

                                    data=jl

                                    Times_compressionCirclesionz=Times_compressionCirclesionz+1

                                   

                                    if countraz==1:



                                        lenf5=len(data)



                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    lenf=len(INFO)



                                    lenf1=len(data)

                                

                                    xc=(lenf1*8)-lenf

                                    z=0

                                    if xc!=0:

                                        while z<xc:

                                            INFO="0"+INFO

                                            z=z+1



                                    INFO2=INFO

                                  
                              
                                    lenf3=len(INFO2)

                                lenf2=len(INFO2)



                                INFO11=""

                                INFO12=""

                                long21=len(INFO3)

                                limit1=0

                                INFO4="'"

                                

                                Times_of_times=0


                                while limit1!=1:    

                                

                                    INFO4=INFO2

                                    long_B=len(INFO4)

                                    long=len(INFO4)

                                    Times_of_times+=1

                                    if Times_of_times==100:

                                        limit1

                                    info_hex=INFO4

                                    times10=0 

                                    limit=0
                                    while times10!=1:

                                        INFO3=info_hex

                                 



                                       

                                        

                                        long=len(INFO3)

                                        #print(long)

                                        

                                        

                                        #print(long)

                                       

                                       

                                        block=0

                                        

                                        blocks=21

                                        #print(blocks)

                                        

                                       

                                        Circle=""

                                        INFO3=INFO2

                                        F=0

                                        F1=0

                                        Times4=0

                                        stop=0

                                        C3=0

                                        S4=""

                                        S9=0

                                        S10=""

                                        S8=""

                                        S18=""
                                        

                                        while block<long:

                                        	

                                            D=0

                                            S1=""

                                            Zigzag_rle=INFO3[block:block+6]
                                            #print(block)

                                        

                                            	

                                          

                                            times_1=0
                                            #print(times_1)

                                            times_2=-4

                                            times_3=0

                                            times_5=0

                                            C4=0

                                            S4=""

                                            times_31=-4

                                            S12=""

                                            sw=""

                                            S15=""

                                            S16=0
                                            C5=0

                                            while times_1!=2:
                                                
                                                times_1+=2
                                                #print(times_1)
                                              
                                                    #print(times_1)
                                                if len(Zigzag_rle[times_1:times_1+2])!=0:
                                            	    times_3=int(Zigzag_rle[times_1:times_1+3],2)
                                            	    C5=1
                                                if times_3-(times_1//2)==0 and C5==1 and len(Zigzag_rle)>=6 and stop==0:
                                                    if len(Zigzag_rle[times_1:times_1+3])==3:
                                                        S11="0"
                                                        Zigzag_rle1=Zigzag_rle[:times_1+1]+S11+Zigzag_rle[times_1+3:]
                                                        Zigzag_rle2=Zigzag_rle1[2:4]+Zigzag_rle1[0:2]+Zigzag_rle1[4:6]
                                                    D=1
                                                    C8=Zigzag_rle2
                                                    Times4+=1
                                                    
                                                    if Zigzag_rle2[2:5]!="001":
                                                        C8=Zigzag_rle
                                                        #print(Zigzag_rle)
                                                        if Zigzag_rle[1:2]=="0":
                                                            stop=1	                                            				                                            			    
                                                elif Zigzag_rle[times_1+1:times_1+2]=="0" and  len(Zigzag_rle)>=6 and stop==0:
	                                            			    times_3=int(Zigzag_rle[times_1:times_1+2],2)
	                                            			    if len(Zigzag_rle[times_1:times_1+2])==2:
	                                            			        S11=format(times_1//2,'01b')
	                                            			        #print(S11)
	                                            			        S12=Zigzag_rle[times_1:times_1+1]
	                                            			        Zigzag_rle1=Zigzag_rle[:times_1+1]+S11+Zigzag_rle[times_1+2:]
	                                            			        Zigzag_rle2=Zigzag_rle1[2:4]+Zigzag_rle1[0:2]+Zigzag_rle1[4:6]
	                                            			    
	                                            			    C8=Zigzag_rle2
	                                            			    Times4+=1
	                                            			    if Zigzag_rle2[2:5]!="001":
	                                            			        C8=Zigzag_rle
	                                            			    
	                                            			    
	                                            			    
	                                            			 
	                                            			    D=2
	                                            			    #print(Zigzag_rle2)
	                                            			    
                                                else:
                                            	    S18=INFO3[block:block+6]
                                            	    C8=S18
                                            	    #print(S18)
                                            	                               

                                       

                                            	


                                           

                                       
                                            D=0
                                            times10+=1
                                            Circle+=C8
                                            block+=32
                                            #print(block)

                                       
                                      
                                            

                                        info_hex="1"+Circle
                                        encypthion=info_hex
                                        INFO14=""
                                        INFO12=encypthion
                                        long21=len(INFO12)
                                        CS=format(Times4,'032b')
                                        INFO11=CS+INFO12
                                        #print(len(INFO2))
                                        if Times55==(2**48)-1 or len(INFO2)==len(INFO11):
                                            
                                            Times56=1                                        
                                        INFO2=INFO11
                                       
                                        Times55+=1

                                        if Times56==1:
                                            CS=format(Times55,'048b')
                                            INFO11="1"+INFO11
                                            lenf=len(INFO11)
                                            add_bits118=""
                                            count_bits=8-lenf%8
                                            z=0
                                            if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                            z=0
                                            INFO11=CS+add_bits118+INFO11
                                            n = int(INFO11, 2)
                                            binary_to_data=len(INFO11)
                                            binary_to_data=(binary_to_data/8)*2
                                            binary_to_data=str(binary_to_data)
                                            binary_to_data="%0"+binary_to_data+"x"
                                            jl=binascii.unhexlify(binary_to_data % n)
                                      
                        
                                            Times_2=10
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)



    def encypthion2(self):



                 

                 if namez=="e":

                    

                    name = input("What is name of file? ")

                    if os.path.exists(name):

                            print('Path is exists!')

                    else:

                            print('Path is not exists!')

                            raise SystemExit

                   

                    namea=""

                    namem=""

                    namema="?"

                    Times55=0

                    Cicle55=0

                    Combination=-1

                    Combination1=-1

                 

                    Times_of_compressionression_2 =0

                    nameas=name

                    nac=len(nameas)

                    name_cut=""

                    name_cut=len(".bin")

                    nameas=name

                    

                    name_long=len(nameas)

                    nameSS=name[name_long-name_cut:]

                    if nameSS!=".bin":

                        x3=0.0

                        return print(x3)

                        

                    nameas=name[:name_long-name_cut]

                    nac=len(nameas)

                    long=len(nameas)
                    nac=len(nameas)
                    countraz=0

                    Circles_functions=2

                    Circles_functions1=0

                    s=""

                    Calculusadd=""
                    INFO3=""

                    INFO2=""

                    Circle55=0



                    ssCircles_functions=0

                    qTimes_compressionCirclesionzl=0
                    block=1


                    x=0

                    x1=0

                    x2=0

                    x = time()



                    with open(nameas, "w") as f4:

                            f4.write(s)

                    with open(nameas, "a") as f3:

                            f3.write(s)

                    with open(name, "rb") as binary_file:



                       # Read the whole file at once

                        

                        data = binary_file.read()


                        if len(data)==0:

                            x4=0.0

                            print(x4)

                            raise SystemExit

                     	



                        s=str(data)

                       

                        lenf1=len(data)

                        lenf5=len(data)

                        

                        Times_2=0

                        Times_compressionCirclesionz=0

                       

                        while Times_2<10:


                            Circles_functions=Circles_functions+1

                            

                            countraz=countraz+1



                            with open(nameas, "ab") as f2:

                                if countraz==1:

                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    lenf=len(INFO)

                                    lenf1=len(data)

                                

                                    xc=(lenf1*8)-lenf

                                    z=0

                                    if xc!=0:

                                        while z<xc:

                                            INFO="0"+INFO

                                            z=z+1


                                    if countraz==1:

                                        INFO2=INFO

                            

                                    n = int(INFO2, 2)

                                

                                    binary_to_data=len(INFO2)

                                    binary_to_data=(binary_to_data/8)*2

                                    binary_to_data=str(binary_to_data)

                                    binary_to_data="%0"+binary_to_data+"x"

                             

                                    jl=binascii.unhexlify(binary_to_data % n)

                                    long6=len(jl)

                                    

                                    data=jl

                                    Times_compressionCirclesionz=Times_compressionCirclesionz+1

                                   

                                    if countraz==1:



                                        lenf5=len(data)



                                    INFO=bin(int(binascii.hexlify(data),16))[2:]

                                    lenf=len(INFO)



                                    lenf1=len(data)

                                

                                    xc=(lenf1*8)-lenf

                                    z=0

                                    if xc!=0:

                                        while z<xc:

                                            INFO="0"+INFO

                                            z=z+1



                                    INFO2=INFO

                                    if countraz==1:                               

	                                    Times_count=12

	                                    #print(Times_count)

	                                  

	                                    while INFO2[0:1]!="1":

	                                    

		                                    if INFO2[0:1]=="0":

		                                    	INFO2=INFO2[1:]

	                                    lenf3=len(INFO2)

	                                    INFO2=INFO2[1:]

	                                    INFO3=INFO2

	                                    Time_count2=0                       

                                lenf2=len(INFO2)

                                INFO11=""

                                INFO12=""

                                long21=len(INFO3)

                                limit1=0

                                INFO4="'"

                                Times_of_times=0

                                while limit1!=1:    

                                    INFO4=INFO2

                                    long_B=len(INFO4)

                                    long=len(INFO4)

                                    Times_of_times+=1

                                    if Times_of_times==100:

                                        limit1
                                

                                    info_hex=INFO4

                                    times10=0 

                                    limit=0
                                    

                                    while times10!=1:

                                        INFO3=info_hex
                                        long=len(INFO3)
                                      

                                        block=0

                                        

                                        blocks=21


                                        Circle=""

                                        INFO3=INFO2

                                        while block<long:

	                                        Zigzag_rle2=INFO3[block:block+1]

	                                        

	                                        if Zigzag_rle2[:1]=="1":

	                                         		                  		Zigzag_rle3=INFO3[block:block+22]

	                                         		                  		Circle+=Zigzag_rle3[1:]

	                                         		                  		block+=22

	                                        elif Zigzag_rle2[:1]=="0":

	                                        	Zigzag_rle3=INFO3[block:block+19]

	                                        	Circle+="00"+Zigzag_rle3

	                                        	block+=19

                                      

                                        times10+=1                                     
                                        info_hex=Circle 

                                        long_after_compressionCirclesion=len(info_hex)

                                        if long==long_after_compressionCirclesion:

                                            limit=1

                                            limit1=1

                                        info_hex=Circle

                                    encypthion=info_hex

                                    INFO14=""

                                    INFO12=encypthion

                                    long21=len(INFO12)

                                

                                    limit1=1
                         

                                Stop_save=""


                                INFO11=INFO12
                                INFO2=INFO11
          	
                                Times55+=1
                                Times_compressionCirclesionz=Times_compresionCirclesionz+1
                                Times_of_compressionression_2=Times_of_compressionression_2 +1
                                if Times55==1:
                                	n = int(INFO11, 2)
                                	binary_to_data=len(INFO11)
                                	binary_to_data=(binary_to_data/8)*2
                                	binary_to_data=str(binary_to_data)
                                	binary_to_data="%0"+binary_to_data+"x"
                                	jl=binascii.unhexlify(binary_to_data % n)
                                	f2.write(jl)
                                	x2 = time()
                                	x3=x2-x
                                	return print(x3)                            
self=""                                
d=encypthion_class()
xw=d.encypthion1()
print(xw)
xw1=d.encypthion2()
print(xw1)