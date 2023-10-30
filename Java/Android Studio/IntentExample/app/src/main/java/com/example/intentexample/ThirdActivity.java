package com.example.intentexample;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class ThirdActivity extends AppCompatActivity {

    private Button thirdBTN;
    private EditText thirdInformation;
    private TextView thirdLBL;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);

        thirdBTN = findViewById(R.id.thirdBTN);
        thirdInformation = findViewById(R.id.thirdUI);
        thirdLBL = findViewById(R.id.thirdLBL);

        thirdBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(ThirdActivity.this,MainActivity.class);

                //step 4: go to it
                startActivity(i);
            }
        });
    }
}
