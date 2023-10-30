public class FixParkerTyPohlsCode {

    public static void main(String[] args) {

        System.out.println(replaceStuff("I like potatos with potato tots and potato things", "potato","brother"));
    }
    public static String replaceStuff(String phrase,String wordToFind,String replace){
        System.out.println(phrase);
        String out="";
        int beginIndex=0;
        while(phrase.indexOf(wordToFind) != -1){         //loop while indexOf(f) finds an f
            String phrase2 = phrase.substring(beginIndex,phrase.indexOf(wordToFind)-1);
            System.out.println(phrase2);
            out += phrase2 + " " + replace;
            System.out.println(out);
            beginIndex = phrase2.length();
            phrase2 = "";
            phrase2 = phrase.substring(beginIndex+replace.length(),out.length()+phrase.indexOf(wordToFind)-1 );
            out += phrase2  + replace;
            System.out.println(out);
            beginIndex = out.length()-2;
            phrase2 = "";
            phrase2 = phrase.substring(beginIndex, out.length()+wordToFind.length()+1 );
            out += phrase2 + " " + replace;
            phrase2 = "";
            beginIndex = out.length()-3;
            phrase2 = phrase.substring(beginIndex);
            out += phrase2 ;
            System.out.println(out);
            break;
        }
        return out;
   }
}