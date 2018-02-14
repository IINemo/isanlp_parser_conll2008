from isanlp.processor_malt_parser import ProcessorParserMalt

class ProcessorParserConll2008(ProcessorParserMalt):
    def __init__(self):
        super().__init__('''java -cp /src/parser_conll2008/ensemble/ensemble-2010-04-19.jar:/src/parser_conll2008/ensemble/lib/log4j-1.2.15.jar:/src/parser_conll2008/ensemble/lib/liblinear-1.33-with-deps.jar \
edu.stanford.nlp.parser.ensemble.maltparser.Malt \
-gds T.TRANS+A.DEPR+A.PPLIFTED -m parse -w /src/parser_conll2008/ensemble/models/default/ -c conll08-covnonproj-ltr''')
        