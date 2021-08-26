package com.example.machinelearningbasedapplicationforforecastingmoviestvseriessuccess;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.animation.ObjectAnimator;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.example.machinelearningbasedapplicationforforecastingmoviestvseriessuccess.Services.MainActivityAdmin;
import com.example.machinelearningbasedapplicationforforecastingmoviestvseriessuccess.Services.MainActivityNonRegisterUser;

public class SplashScreen extends AppCompatActivity {

    ProgressBar splashProgress;
    ImageView wal,logo;
    TextView title;
    int SPLASH_TIME = 3000; //This is 3 seconds


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);

        title=findViewById(R.id.title);



        Animation animaton=AnimationUtils.loadAnimation(this,R.anim.fade_transition_animation);
        title.startAnimation(animaton);


        wal = findViewById(R.id.wal);
        Glide.with(this).load(R.drawable.splashscreenwalpaper)
                .placeholder(R.drawable.ic_launcher_background)
                .error(R.drawable.ic_launcher_background)
                .into(wal);


        logo = findViewById(R.id.logo);
        Glide.with(this).load(R.mipmap.ic_latestlauncherapp_foreground)
                .placeholder(R.drawable.ic_launcher_foreground)
                .error(R.drawable.ic_launcher_foreground)
                .into(logo);




        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {

                Intent mySuperIntent = new Intent(SplashScreen.this, WelcomeActivity.class);
                startActivity(mySuperIntent);


                finish();

            }
        }, SPLASH_TIME);
    }






    }
