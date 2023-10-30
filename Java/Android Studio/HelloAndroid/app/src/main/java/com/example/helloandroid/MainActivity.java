package com.example.helloandroid;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    //creating a function or method for the button to do something
    public void sayHello(View v) {
        //View v -> is an object of the view class which assist the button to find this f(x)
        // This goes back to the Model View Controller set up or Game loop in Love2d
        // v will now allow the XML to see the f(x)
        // YOU MUST DO THIS for using an onClick

        //obtain the info from the widgets
        EditText userInput = findViewById(R.id.editUserInput);
        TextView greetingText = findViewById(R.id.outputTextView);

        //output something to the outputTextView
        greetingText.setText("Hi " + userInput.getText() + ", nice to meet you!");
    }
}

