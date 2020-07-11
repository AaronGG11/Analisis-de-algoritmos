import java.util.ArrayList;
import java.util.Scanner;

public class Transformada{

    public static ArrayList<Complex> calcular(ArrayList<Complex> a){
        int n = a.size();
        if( n == 1){
            return a;
        }

        Complex w = new Complex(1,0);
        Complex wn = new Complex(Math.cos(2*Math.PI/n),Math.sin(2*Math.PI/n));
        ArrayList<Complex>pares = new ArrayList<Complex>();
        ArrayList<Complex>impares = new ArrayList<Complex>();

        ArrayList<Complex> y = new ArrayList();
        for(int i = 0; i < n; i++){
            if(i % 2 == 0){
                pares.add(a.get(i));
            }
            else{
                impares.add(a.get(i));
            }
        }

        for(int i=0;i<n;i++)y.add(new Complex(0,0));

        pares = calcular(pares);
        impares = calcular(impares);

        for(int k = 0; k <=  (n/2)-1 ; k++){

            y.set(k,Complex.plus(pares.get(k), impares.get(k).times(w)));
            y.set(k+(n/2),pares.get(k).minus(impares.get(k).times(w)));
            w = w.times(wn);
        }
        return y;
    }  
    
       public static ArrayList<Complex>leerPolinomio(int grado){

        Scanner x = new Scanner(System.in);
        double aux,aux2;

        ArrayList<Complex> poli = new ArrayList<Complex>();

        for(int i = 0 ; i < grado; i++){

            aux = x.nextDouble();
            aux2 = x.nextDouble();

    
            poli.add(new Complex(aux,aux2)) ;

        }   

        return poli;
        

    }
    
    public static ArrayList<Complex>sumar(ArrayList<Complex> a , ArrayList<Complex> b){

        ArrayList<Complex> respuesta = new ArrayList<Complex>();

        for(int i=0 ; i < a.size(); i++){

            respuesta.add(Complex.plus(a.get(i),b.get(i)));
        }

        return respuesta;
        
    }
    
    public static ArrayList<Complex> multiplicar(ArrayList<Complex> a , ArrayList<Complex> b){

        ArrayList<Complex> mult = new ArrayList<Complex>();
        ArrayList<Complex> respuesta = new ArrayList<Complex>();

        for(int i=0;i<a.size()+b.size()-1;i++)respuesta.add(new Complex(0,0));

        for(int i=0;i<a.size();i++){

            for(int j=0;j<b.size();j++){

                mult.set(i+j, Complex.plus(respuesta.get(i+j), a.get(i).times(b.get(j))));
            }
        }
        
        respuesta = Transformada.calcular(mult);

        return respuesta;
    }
    
    public static void imprimir(ArrayList<Complex> r){

        for(int i=0;i<r.size();i++){

            System.out.println(r.get(i));
        }
    }
    
    public static void main(String[] args){

        ArrayList<Complex> a = new ArrayList<Complex>();
        a.add(new Complex(0,0));
        a.add(new Complex(0,0));
        a.add(new Complex(0,0));
        a.add(new Complex(0,0));
        a.add(new Complex(0,0));
        a.add(new Complex(1,0));
        
        ArrayList<Complex> b = new ArrayList<Complex>();
        b.add(new Complex(2,0));
        b.add(new Complex(0,0));
        b.add(new Complex(0,0));
        b.add(new Complex(1,0));
        
        //ArrayList<Complex> r = TransformadaRF.calcular(a);
        System.out.println("Arreglo ingresado: "+a);
        System.out.println("");
        System.out.println("Arreglo ingresado: "+b);
        System.out.println("");
        
        ArrayList<Complex> r = Transformada.sumar(a, b);
        
        //System.out.println("resultado: "+r);
        
    }
}