package com.example.madlibapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        TextView BirthdayLibTXT = findViewById(R.id.birthdayLib);

        Intent intent = getIntent();
        String adj1 = intent.getStringExtra("adj1");
        String adj2 = intent.getStringExtra("adj2");
        String adj3 = intent.getStringExtra("adj3");
        String noun1 = intent.getStringExtra("noun1");
        String noun2 = intent.getStringExtra("noun2");
        String verb1 = intent.getStringExtra("verb1");
        String verb2 = intent.getStringExtra("verb2");
        String adverb1 = intent.getStringExtra("adverb1");
        String name1 = intent.getStringExtra("name1");




        BirthdayLibTXT.setText("The Birthday Surprise: Today is " + name1 +"'s " + adj1 + " birthday! " + name1 + " woke up to a room filled with " + adj2 + " balloons and a " + adj3 + " cake. "
                         + name1 +" was " + adverb1 + " excited! For presents, " + name1 + " received a " + noun1 + " and a " + noun2 + ". They couldn't wait to " + verb1 + " with them. " +
                "Later, " + name1 + " and their friends " + verb2 + " around the " + noun1 + ", " + verb1 + " and " + verb2 + " until the sun ducks below the horizon.");

    }
}