/**
 * Song
 */
import java.util.Scanner;

public class Song {

    String song, artist;
    double rating, duration;

    public Song(){

    }

    public Song(String songName){
        this.song = songName;
    }

    public Song(String songName, String artistName){
        this.song = songName;
        this.artist = artistName;
    }
    
    public Song(String songName, String artistName, double rate){
        this.song = songName;
        this.artist = artistName;
        this.rating = rate;
    }

    public Song(String songName, String artistName, double rate, double time){
        this.song = songName;
        this.artist = artistName;
        this.rating = rate;
        this.duration = time;
    }

    //getters & setters
    //accessors & mutators
    //will have a getter and setter for each field variable

    public void setName(String newSong){
        this.song=newSong;
    }
    public String getName(){
        return this.song;
    }

    public void setRating(double newRating){
        this.rating=newRating;
    }

    public double getRating(){
        return this.rating;
    }

    public void setDuration(double newDuration){
        this.duration = newDuration;
    }

    public double getDuration(){
        return this.duration;
    }




    @Override
    public String toString() {
        String out="";
        out+="Title: "+this.song;
        out+="\nArtist: "+this.artist;
        out+="\nRating: "+this.rating;
        out+="\nTime: "+this.duration;
        out+="\n";
        return out;
    }
}