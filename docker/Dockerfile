FROM inemo/isanlp

ENV PARSER_CONLL2008=/src/parser_conll2008/

COPY ensemble.tar.gz $PARSER_CONLL2008
RUN cd $PARSER_CONLL2008 && tar -xf ensemble.tar.gz
COPY models.tar.gz $PARSER_CONLL2008/ensemble
RUN cd $PARSER_CONLL2008/ensemble/ && tar -xf models.tar.gz

COPY src $PARSER_CONLL2008

CMD [ "python", "/start.py", "-m parser_conll2008 -a PipelineConll2008()" ]

