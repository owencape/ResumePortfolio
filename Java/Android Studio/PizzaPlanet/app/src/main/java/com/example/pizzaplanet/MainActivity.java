package com.example.pizzaplanet;

import static android.widget.Toast.*;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        CheckBox cheCB = findViewById(R.id.cheCB);
        CheckBox pepCB = findViewById(R.id.pepCB);
        CheckBox sauCB = findViewById(R.id.sauCB);
        Button orderBTN = findViewById(R.id.orderBTN);
        RadioGroup rbGroup = findViewById(R.id.radioGroup);
        RadioButton smallRB = findViewById(R.id.smallRB);
        RadioButton medRB = findViewById(R.id.medRB);
        RadioButton larRB = findViewById(R.id.larRB);

        orderBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String order = "";
                String topping = "";

                if (cheCB.isChecked()) {
                    TextView t = findViewById(R.id.textView);
                    topping = "cheese";
                } else if (pepCB.isChecked()) {
                    TextView t = findViewById(R.id.textView);
                    topping = "pepperoni";
                } else if (sauCB.isChecked()) {
                    TextView t = findViewById(R.id.textView);
                    topping = "sausage";
                }

                if (smallRB.isChecked()) {
                    order = "Small " + topping + " Pizza";
                } else if (medRB.isChecked()) {
                    order = "Medium " + topping + " Pizza";
                } else if (larRB.isChecked()) {
                    order = "Large " + topping + " Pizza";
                }

                // makeText(in which activity, the message, short or long).show()
                Toast.makeText(MainActivity.this, order, Toast.LENGTH_LONG).show();
            }
             });





    }
}