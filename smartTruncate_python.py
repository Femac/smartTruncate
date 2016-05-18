#!/usr/bin/python

def smartTruncate(content, begin=0, length=100, addSuffix=False, suffix=' ...', addPrefix=False, prefix='... '):
        '''Truncate a string without cutting a sentence in the middle.
        Syntax: smartTruncate(content, begin=0, length=100, addSuffix=False, suffix=' ...', addPrefix=False, prefix='... ')
        Returns dictionary object with trimmed string 'result' and the index value where it ended 'trimmed_at_index'
        '''

        def finalize(string, wasChanged=False):
                'This function adds the prefix and suffix and builds the return object'
                if wasChanged:
                        #if a begin value was given, and prefix was requested, add prefix
                        if begin != 0 and addPrefix is True:
                                string = ''.join([prefix, string])
                        #if suffix was requested, add suffix
                        if addSuffix is True:
                                string = ''.join([string, suffix])
                        #if it was trimmed, include that in the result set
                        if end_of_sentence:
                                return {'result': string,'trimmed_at_index': end_of_sentence + 1}
                        else:   
                                return {'result': string}
                #if it wasn't changed then just return the string
                else:
                        return {'result': string}

        #cut beginning value from content
        if begin != 0:
                mod_content = content[begin:]
                wasChanged = True
        #make sure variable mod_content is created
        else:   
                mod_content = content

        #if content.length is less than desired length then return the content unmodified
        if len(mod_content) <= length:
                return finalize(mod_content, wasChanged)

        #else if the content.length is longer than desired length then:
        else:   
                #first, trim character count to desired length
                mod_content = content[0:length-1]
                #add a trailing space in case the final character is a period and we already ended on a perfect sentence boundary
                mod_content = ''.join([mod_content,' '])
                #second, find the last-most period or sentence termination including the period
                end_of_sentence = mod_content.rfind('. ')+1
                #third, trim to the last full sentence
                mod_content = content[0:end_of_sentence+1]
                #final, return the modified content
                return finalize(mod_content, wasChanged=True)
