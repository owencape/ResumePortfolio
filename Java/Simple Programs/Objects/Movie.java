public class Movie {
    
    String name,author;

    double rate;

    public Movie(){};

    public Movie(String title){
        this.name = title;
    }

    public Movie(String title, String author){
        this.name = title;
        this.author = author;
    }

    public Movie(String title, String author, double rate){
        this.name = title;
        this.author = author;
        this.rate = rate;
    }

    @Override
    public String toString() {
        String out="";
        out+="title: "+this.name;
        out+="author: "+this.author;
        out+="rating: "+this.rate;
        return out;
    }


}
