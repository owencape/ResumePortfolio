package com.example.madlibandroidapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

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
        EditText nounTXT2 = findViewById(R.id.noun2Text);
        EditText verb1TXT = findViewById(R.id.verb1Text);
        EditText verb2TXT = findViewById(R.id.verb2Text);
        EditText adverbTXT = findViewById(R.id.adverbText);
        EditText nameTXT = findViewById(R.id.nameText);
        Button opt1BTN = findViewById(R.id.option1);
        Button opt2BTN = findViewById(R.id.option2);
        Button opt3BTN = findViewById(R.id.option3);
        Button randomBTN = findViewById(R.id.randoOptionBTN);
        TextView outputTXT = findViewById(R.id.MadLibText);

        option1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Random rand = new Random();

                String first = String.valueOf(firstETXT.getText());
                String last = String.valueOf(lastETXT.getText());
                String city = String.valueOf(cityETXT.getText());
                String school = String.valueOf(schoolETXT.getText());
                String pet = String.valueOf(petETXT.getText());
                String sibling = String.valueOf(siblingETXT.getText());




                int firstPortion = rand.nextInt(first.length());
                int lastPortion = rand.nextInt(last.length());
                String scifiFirst = first.substring(0, firstPortion) + last.substring(0, lastPortion);
                firstPortion = rand.nextInt(city.length());
                lastPortion = rand.nextInt(school.length());
                String scifiLast = city.substring(0, firstPortion) + school.substring(0, lastPortion);
                firstPortion = rand.nextInt(pet.length());
                lastPortion = rand.nextInt(sibling.length());
                String scifiOrigin = pet.substring(0, firstPortion) + sibling.substring(0, lastPortion);
                outputTXT.setText(scifiFirst+" "+scifiLast+" of the planet "+scifiOrigin);
            }
    }
}