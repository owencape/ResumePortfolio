package com.example.madlibapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.Random;

public class MainActivity extends AppCompatActivity {




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText adj1TXT = findViewById(R.id.adjective1Text);
        EditText adj2TXT = findViewById(R.id.adjective2Text);
        EditText adj3TXT = findViewById(R.id.adjective3Text);
        EditText noun1TXT = findViewById(R.id.noun1Text);
        EditText noun2TXT = findViewById(R.id.noun2Text);
        EditText verb1TXT = findViewById(R.id.verb1Text);
        EditText verb2TXT = findViewById(R.id.verb2Text);
        EditText adverbTXT = findViewById(R.id.adverbText);
        EditText nameTXT = findViewById(R.id.nameText);
        Button nextActivityBirthdayBTN = findViewById(R.id.birthdayBTN);
        Button nextActivityJungleBTN = findViewById(R.id.jungleBTN);
        Button nextActivitySuperheroBTN = findViewById(R.id.SuperheroBTN);
        Button nextActivityRandomBTN = findViewById(R.id.randomBTN);


        nextActivityRandomBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                int choice = 0;

                

                if (choice==1){
                    madLib1();
                }
                else if (choice==2){
                    madLib2();
                }
                else if (choice==3){
                    madLib3();
                }


            }
        });

//        nextActivityBirthdayBTN.setOnClickListener(v -> {
//            Intent intent = new Intent(MainActivity.this, MainActivity2.class);
//            startActivity(intent);
//        });

//        nextActivityJungleBTN.setOnClickListener(v -> {
//            Intent intent = new Intent(MainActivity.this, MainActivity3.class);
//            startActivity(intent);
//        });

//        nextActivitySuperheroBTN.setOnClickListener(v -> {
//            Intent intent = new Intent(MainActivity.this, MainActivity4.class);
//            startActivity(intent);
//        });

        nextActivityBirthdayBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String adj1 = String.valueOf(adj1TXT.getText());
                String adj2 = String.valueOf(adj2TXT.getText());
                String adj3 = String.valueOf(adj3TXT.getText());
                String noun1 = String.valueOf(noun1TXT.getText());
                String noun2 = String.valueOf(noun2TXT.getText());
                String verb1 = String.valueOf(verb1TXT.getText());
                String verb2 = String.valueOf(verb2TXT.getText());
                String adverb1 = String.valueOf(adverbTXT.getText());
                String name1 = String.valueOf(nameTXT.getText());

                Intent intent = new Intent(MainActivity.this,MainActivity2.class);
                intent.putExtra("adj1",adj1);
                intent.putExtra("adj2",adj2);
                intent.putExtra("adj3",adj3);
                intent.putExtra("noun1",noun1);
                intent.putExtra("noun2",noun2);
                intent.putExtra("verb1",verb1);
                intent.putExtra("verb2",verb2);
                intent.putExtra("adverb1",adverb1);
                intent.putExtra("name1",name1);
                startActivity(intent);
            }
        });

        nextActivityJungleBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String adj1 = String.valueOf(adj1TXT.getText());
                String adj2 = String.valueOf(adj2TXT.getText());
                String adj3 = String.valueOf(adj3TXT.getText());
                String noun1 = String.valueOf(noun1TXT.getText());
                String noun2 = String.valueOf(noun2TXT.getText());
                String verb1 = String.valueOf(verb1TXT.getText());
                String verb2 = String.valueOf(verb2TXT.getText());
                String adverb1 = String.valueOf(adverbTXT.getText());
                String name1 = String.valueOf(nameTXT.getText());

                Intent intent = new Intent(MainActivity.this,MainActivity3.class);
                intent.putExtra("adj1",adj1);
                intent.putExtra("adj2",adj2);
                intent.putExtra("adj3",adj3);
                intent.putExtra("noun1",noun1);
                intent.putExtra("noun2",noun2);
                intent.putExtra("verb1",verb1);
                intent.putExtra("verb2",verb2);
                intent.putExtra("adverb1",adverb1);
                intent.putExtra("name1",name1);
                startActivity(intent);
            }
        });

        nextActivitySuperheroBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String adj1 = String.valueOf(adj1TXT.getText());
                String adj2 = String.valueOf(adj2TXT.getText());
                String adj3 = String.valueOf(adj3TXT.getText());
                String noun1 = String.valueOf(noun1TXT.getText());
                String noun2 = String.valueOf(noun2TXT.getText());
                String verb1 = String.valueOf(verb1TXT.getText());
                String verb2 = String.valueOf(verb2TXT.getText());
                String adverb1 = String.valueOf(adverbTXT.getText());
                String name1 = String.valueOf(nameTXT.getText());

                Intent intent = new Intent(MainActivity.this,MainActivity4.class);
                intent.putExtra("adj1",adj1);
                intent.putExtra("adj2",adj2);
                intent.putExtra("adj3",adj3);
                intent.putExtra("noun1",noun1);
                intent.putExtra("noun2",noun2);
                intent.putExtra("verb1",verb1);
                intent.putExtra("verb2",verb2);
                intent.putExtra("adverb1",adverb1);
                intent.putExtra("name1",name1);
                startActivity(intent);
            }
        });

    }

    EditText adj1TXT = findViewById(R.id.adjective1Text);
    EditText adj2TXT = findViewById(R.id.adjective2Text);
    EditText adj3TXT = findViewById(R.id.adjective3Text);
    EditText noun1TXT = findViewById(R.id.noun1Text);
    EditText noun2TXT = findViewById(R.id.noun2Text);
    EditText verb1TXT = findViewById(R.id.verb1Text);
    EditText verb2TXT = findViewById(R.id.verb2Text);
    EditText adverbTXT = findViewById(R.id.adverbText);
    EditText nameTXT = findViewById(R.id.nameText);
    Button nextActivityBirthdayBTN = findViewById(R.id.birthdayBTN);
    Button nextActivityJungleBTN = findViewById(R.id.jungleBTN);
    Button nextActivitySuperheroBTN = findViewById(R.id.SuperheroBTN);
    Button nextActivityRandomBTN = findViewById(R.id.randomBTN);
    public void madLib1(){

        String adj1 = String.valueOf(adj1TXT.getText());
        String adj2 = String.valueOf(adj2TXT.getText());
        String adj3 = String.valueOf(adj3TXT.getText());
        String noun1 = String.valueOf(noun1TXT.getText());
        String noun2 = String.valueOf(noun2TXT.getText());
        String verb1 = String.valueOf(verb1TXT.getText());
        String verb2 = String.valueOf(verb2TXT.getText());
        String adverb1 = String.valueOf(adverbTXT.getText());
        String name1 = String.valueOf(nameTXT.getText());

        Intent intent = new Intent(MainActivity.this,MainActivity2.class);
        intent.putExtra("adj1",adj1);
        intent.putExtra("adj2",adj2);
        intent.putExtra("adj3",adj3);
        intent.putExtra("noun1",noun1);
        intent.putExtra("noun2",noun2);
        intent.putExtra("verb1",verb1);
        intent.putExtra("verb2",verb2);
        intent.putExtra("adverb1",adverb1);
        intent.putExtra("name1",name1);
        startActivity(intent);
    }

    public void madLib2(){

        String adj1 = String.valueOf(adj1TXT.getText());
        String adj2 = String.valueOf(adj2TXT.getText());
        String adj3 = String.valueOf(adj3TXT.getText());
        String noun1 = String.valueOf(noun1TXT.getText());
        String noun2 = String.valueOf(noun2TXT.getText());
        String verb1 = String.valueOf(verb1TXT.getText());
        String verb2 = String.valueOf(verb2TXT.getText());
        String adverb1 = String.valueOf(adverbTXT.getText());
        String name1 = String.valueOf(nameTXT.getText());

        Intent intent = new Intent(MainActivity.this,MainActivity3.class);
        intent.putExtra("adj1",adj1);
        intent.putExtra("adj2",adj2);
        intent.putExtra("adj3",adj3);
        intent.putExtra("noun1",noun1);
        intent.putExtra("noun2",noun2);
        intent.putExtra("verb1",verb1);
        intent.putExtra("verb2",verb2);
        intent.putExtra("adverb1",adverb1);
        intent.putExtra("name1",name1);
        startActivity(intent);
    }

    public void madLib3(){

        String adj1 = String.valueOf(adj1TXT.getText());
        String adj2 = String.valueOf(adj2TXT.getText());
        String adj3 = String.valueOf(adj3TXT.getText());
        String noun1 = String.valueOf(noun1TXT.getText());
        String noun2 = String.valueOf(noun2TXT.getText());
        String verb1 = String.valueOf(verb1TXT.getText());
        String verb2 = String.valueOf(verb2TXT.getText());
        String adverb1 = String.valueOf(adverbTXT.getText());
        String name1 = String.valueOf(nameTXT.getText());

        Intent intent = new Intent(MainActivity.this,MainActivity4.class);
        intent.putExtra("adj1",adj1);
        intent.putExtra("adj2",adj2);
        intent.putExtra("adj3",adj3);
        intent.putExtra("noun1",noun1);
        intent.putExtra("noun2",noun2);
        intent.putExtra("verb1",verb1);
        intent.putExtra("verb2",verb2);
        intent.putExtra("adverb1",adverb1);
        intent.putExtra("name1",name1);
        startActivity(intent);
    }




}