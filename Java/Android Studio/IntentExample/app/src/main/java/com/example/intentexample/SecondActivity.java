package com.example.intentexample;

import android.content.Intent;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    private Button secondBTN;
    private EditText secondInformation;
    private TextView secondLabel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        secondBTN = findViewById(R.id.secondBTN);
        secondInformation = findViewById(R.id.secondUI);
        secondLabel = findViewById(R.id.secondLBL);
        String dataFromPageOne = getIntent().getStringExtra("user input");
        secondLabel.setText(dataFromPageOne);

        secondBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(SecondActivity.this,ThirdActivity.class);
                i.putExtra("second user input", (secondInformation.getText())+" "+dataFromPageOne);
                //step 4: go to it
                startActivity(i);
            }
        });
    }
}
