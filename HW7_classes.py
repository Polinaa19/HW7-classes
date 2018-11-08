class Dna(str):
    def __init__(self, sequence_Dna):
        self.sequence_Dna = sequence_Dna.upper()

        nucleotides = 'ATCG'
        for i in self.sequence_Dna:
            if i not in nucleotides:
                raise Exception('Your string is not DNA sequence.')

    def gc(self):
        gc_content = str(round((self.sequence_Dna.count('G') + self.sequence_Dna.count('C')) * 100 / len(self.sequence_Dna), 2)) + '%'
        return gc_content

    def reverse_complement(self):
        reverse_complement_sequence = self.sequence_Dna.translate(self.sequence_Dna.maketrans('ATGC', 'TACG'))
        return reverse_complement_sequence[::-1]

    def transcribe(self):
        self.sequence_Rna = self.sequence_Dna.translate(self.sequence_Dna.maketrans('ATGC', 'UACG'))
        return self.sequence_Rna


class Rna(str):
    def __init__(self, sequence_Rna):
        self.sequence_Rna = sequence_Rna.upper()

        nucleotides = 'AUCG'
        for i in self.sequence_Rna:
            if i not in nucleotides:
                raise Exception('Your string is not RNA sequence.')

    def gc(self):
        gc_content = str(round((self.sequence_Rna.count('G') + self.sequence_Rna.count('C'))*100/len(self.sequence_Rna), 2)) + '%'
        return gc_content

    def reverse_complement(self):
        reverse_complement_sequence = self.sequence_Rna.translate(self.sequence_Rna.maketrans('AUGC', 'UACG'))
        return reverse_complement_sequence[::-1]
