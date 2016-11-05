package com.example.ajinkya.feeder;

import android.content.Intent;
import android.content.SharedPreferences;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;



import com.squareup.okhttp.Callback;
import com.squareup.okhttp.MediaType;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;




import java.io.IOException;




public class MainActivity extends AppCompatActivity {

    private static final String LOGIN_URL = "http://10.0.2.2:8000/login_app";
    EditText login_name, password;
    Button login;
    private final OkHttpClient client = new OkHttpClient();
    public static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        login_name = (EditText) findViewById(R.id.login_name);
        password = (EditText) findViewById(R.id.password);
        login = (Button) findViewById(R.id.login);

        SharedPreferences prefs = getSharedPreferences("LOGIN", MODE_PRIVATE);
        String name = prefs.getString("name", null);
        String pass = prefs.getString("password", null);
        if (name!=null && pass!=null) {
            login(name, pass);
        }
    }

    public void loginButton(View view) {
        final String name = login_name.getText().toString();
        final String pass = password.getText().toString();
        login(name, pass);
    }

    private void login(final String name, final String pass) {
        if (name.equals("")) {
            Toast.makeText(this, "Please enter name", Toast.LENGTH_SHORT).show();
            return;
        }
        if (pass.equals("")) {
            Toast.makeText(this, "Please enter password", Toast.LENGTH_SHORT).show();
            return;
        }
        //if (jsonData.equals("yes")) {

            // Saving credentials
            SharedPreferences.Editor editor = getSharedPreferences("LOGIN", MODE_PRIVATE).edit();
            editor.putString("name", name);
            editor.putString("password", pass);
            editor.apply();

            Intent intent = new Intent(MainActivity.this, Dashboard.class);
            startActivity(intent);
            finish();
        /**
         * Building JSON which looks like:
         *
         * { "login_nam" : "Ajinkya",
         *   "password" : "abcdef"
         * }
         */

//        String jsonData = "{" +
//                "\"login_name\" : \"" + name + "\",\n" +
//                "\"password\" : \"" + pass + "\"" +
//                "}";
//        RequestBody body = RequestBody.create(JSON, jsonData);
//        Log.d("Login", "Login JSON = " + jsonData);
//
//        Request request = new com.squareup.okhttp.Request.Builder()
//                .url(LOGIN_URL)
//                .post(body)
//                .build();

//        client.newCall(request).enqueue(new Callback() {
//            @Override
//            public void onFailure(com.squareup.okhttp.Request request, IOException throwable) {
//                throwable.printStackTrace();
//            }
//
//            @Override
//            public void onResponse(com.squareup.okhttp.Response response) throws IOException {
//                if (!response.isSuccessful())
//                    throw new IOException("Unexpected code " + response);
//                else {
//                    final String jsonData = response.body().string();
//                    Log.d("MainActivity", "Response from " + LOGIN_URL + ": " + jsonData);
//                    if (jsonData.equals("yes")) {
//
//                        // Saving credentials
//                        SharedPreferences.Editor editor = getSharedPreferences("LOGIN", MODE_PRIVATE).edit();
//                        editor.putString("name", name);
//                        editor.putString("password", pass);
//                        editor.apply();
//
//                        Intent intent = new Intent(MainActivity.this, Dashboard.class);
//                        startActivity(intent);
//                        finish();
//                    } else if (jsonData.equals("Invalid user")) {
//                        runOnUiThread(new Runnable() {
//                                          @Override
//                                          public void run() {
//                                              Toast.makeText(getApplicationContext(), "Invalid name", Toast.LENGTH_SHORT).show();
//                                          }
//                                      }
//                        );
//                    } else if (jsonData.equals("Invalid password")) {
//                        runOnUiThread(new Runnable() {
//                                          @Override
//                                          public void run() {
//                                              Toast.makeText(getApplicationContext(), "Invalid password", Toast.LENGTH_SHORT).show();
//                                          }
//                                      }
//                        );
//                    }
              //  }
            //}
        }
    //);
    }
//}
