#!/usr/bin/env python3

import aws_cdk as cdk

from cloud_movie_recommendation.cloud_movie_recommendation_stack import CloudMovieRecommendationStack


app = cdk.App()
CloudMovieRecommendationStack(app, "CloudMovieRecommendationStack")

app.synth()
