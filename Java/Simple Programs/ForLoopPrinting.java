/**
 * ForLoopPrinting
 */
public class ForLoopPrinting {

    public static void main(String[] args) {

        int t = 0;
        
        for(int x=0;x!=3;x++){
            for(int r=0;r<=2;r+=1){
                
                t +=1;

                if(t!=9){
                    System.out.print(r+",");
                }else{
                    System.out.print(r);
                }
        }
        }

        System.out.println("");
        t = 0;
        for(int x=0;x!=3;x++){
            for(int r=2;r>=0;r-=1){

                t +=1;

                if(t!=9){
                    System.out.print(r+",");
                }else{
                    System.out.print(r);
                }
        }
        }
    }
}