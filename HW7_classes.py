class Dna(str):


    def __init__(self, sequence_Dna):
        self.sequence_Dna = sequence_Dna


    def gc(self):
        GC_content = round((self.count('G') + self.count('C')) * 100 / len(self), 2)
        return print(GC_content, '%')


    def reverse_complement(self):
        complement_sequence = self.translate(self.maketrans('ATGC', 'TACG'))
        return print(complement_sequence)


    def transcribe(self):
        complement_Rna = self.translate(self.maketrans('ATGC', 'UACG'))
        return print(complement_Rna)


class Rna(str):


    def __init__(self, sequence_Rna):
        self.sequence_Rna = sequence_Rna


    def gc(self):
        GC_content = round((self.count('G') + self.count('C')) * 100 / len(self), 2)
        return GC_content


    def reverse_complement(self):
        complement_sequence = self.translate(self.maketrans('AUGC', 'UACG'))
        return print(complement_sequence)