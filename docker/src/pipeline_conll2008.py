from isanlp.pipeline_common import PipelineCommon
from isanlp.en.processor_tokenizer_nltk_en import ProcessorTokenizerNltkEn
from isanlp.processor_sentence_splitter import ProcessorSentenceSplitter
from isanlp.en.processor_postagger_nltk_en import ProcessorPostaggerNltkEn
from isanlp.en.processor_lemmatizer_nltk_en import ProcessorLemmatizerNltkEn
from isanlp.converter_nltk_dep_graph import ConverterNltkDepGraph
from .processor_parser_conll2008 import ProcessorParserConll2008


class PipelineConll2008(PipelineCommon):
    def __init__(self):
        super().__init__({'tokenizer' : (ProcessorTokenizerNltkEn(), 
                                         ['text'], 
                                         {0 : 'tokens'}),
                          'sentence_splitter' : (ProcessorSentenceSplitter(), 
                                                 ['tokens'], 
                                                 {0 : 'sentences'}),
                          'postagger' : (ProcessorPostaggerNltkEn(), 
                                         ['tokens', 'sentences'], 
                                         {0 : 'postag'}),
                          'lemmatizer' : (ProcessorLemmatizerNltkEn(), 
                                          ['tokens', 'sentences', 'postag'], 
                                          {0 : 'lemma'}),
                          'syntax_processor' : (PipelineCommon([(ProcessorParserConll2008(), 
                                                                ['tokens', 'sentences', 'postag'], 
                                                                {0 : 'syn_dep_tree'}),
                                                               (ConverterNltkDepGraph(), 
                                                                ['syn_dep_tree'], 
                                                                {0 : 'syn_dep_tree'})]), 
                                                ['tokens', 'sentences', 'postag'],
                                                {'syn_dep_tree' : 'syn_dep_tree'})
                         }, name = 'default')

