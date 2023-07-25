# Xpo-flask

Flask and blueprint drained my energy so I could not really focus on the other parts. But that reinforced my love for golang where you can just have an executable you embed into container.

Anyway, I could not get blueprint and metrics work leveraging external library. There was circular import problem. So I removed blueprint and use default decorator (@app,route) which somehow worked better for me. Still PUT method does not work, I don't know why. I could not get test running either.

I did not create grafana dashboard because I did not build to dockerfile. But I commented the logic. I know that might be below your expectation.
