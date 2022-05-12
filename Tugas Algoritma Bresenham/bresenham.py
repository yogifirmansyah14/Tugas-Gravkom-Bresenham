# Moch Yogi Firmansyah
# 20051397044
# D4 Manajemen Informatika 2020B

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def BRESENHAM(x1,y1,x2,y2):
    #Menentukan delta X dan delta Y
    x = x1
    y = y1
    deltaX = abs(x2-x1)
    deltaY = abs(y2-y1)

    #Menghitung p, 2dx dan 2(dy-dx)
    p = (2 * deltaY) - (deltaX)
    duadx = 2 * deltaX
    duaDyDx = 2 * (deltaY-deltaX) 

    #Menentukan titik awal dan titik akhir
    if(x1>x2):
        x = x2
        y = y2
        xend = x1
        
    else:
        x = x1
        y = y1
        xend = x2

    #Memulai menggambar menggunakan BRESENHAM
    #Membersihkan window
    glClear(GL_COLOR_BUFFER_BIT)
    #Menentukan warna
    glColor3f(1.0,0.0,0.0)
    #Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(10.0)
    #Memilih mode point
    glBegin(GL_POINTS)

    #Looping pada saat nilai x1 < x2
    while x<xend:
        #Menentukan titik yang akan diisi
        x +=1
        
        if(p<0):
            p+=duadx
        elif(y1>y2):
            y-=1
        else:
            y+=1
            
        p += duaDyDx
        
        #Menggambar pixel
        glVertex2i(x,y)  
    
    glEnd()
    glFlush()

def main():
    x1 = int(10)
    y1 = int(10)
    x2 = int(60)
    y2 = int(60)

    #inisialisasi glut
    glutInit(sys.argv)
    #inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_RGB)
    #inisialisasi ukuran layar glut
    glutInitWindowSize(500,500)
    #inisiasliasi posisi layar glut
    glutInitWindowPosition(0,0)
    #inisialisasi pembuatan window
    glutCreateWindow("Menggambar garis menggunakan BRESENHAM")
    glutDisplayFunc(lambda: BRESENHAM(x1,y1,x2,y2))
    glutIdleFunc(lambda: BRESENHAM(x1,y1,x2,y2))
    
    #Memberihkan layar dan memberikan warna
    glClearColor(0.0,0.0,0.0,1.0)
    #Set origin dari grid dan ukurannya 100 x 100
    gluOrtho2D(0,100,0,100)
    glutMainLoop()
    
main()