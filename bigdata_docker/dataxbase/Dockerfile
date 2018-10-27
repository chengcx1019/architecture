From scalabase



WORKDIR /home/hadoop

COPY ./deps/datax.tar.gz .
RUN mkdir etl
RUN chown hadoop etl -R
RUN tar xzf datax.tar.gz \
    && mv datax etl/ \
    && rm *.gz
RUN mkdir tasks
RUN chown hadoop tasks -R
