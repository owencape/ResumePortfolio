package com.example.intentexample;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    //step 1 list global variables
    private Button first;
    private EditText firstInformation;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //step 2 connect the java obj with the widgets

        first = findViewById(R.id.firstBTN);
        firstInformation = findViewById(R.id.firstUI);

        first.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //step 3: set up your intent
                Intent i = new Intent(MainActivity.this,SecondActivity.class);

                i.putExtra("user input",String.valueOf(firstInformation.getText()));

                //step 4: go to it
                startActivity(i);
            }
        });
    }
}