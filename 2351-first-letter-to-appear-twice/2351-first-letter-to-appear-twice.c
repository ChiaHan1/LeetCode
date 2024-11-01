char repeatedCharacter(char* s) {
    uint32_t bitmap = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (bitmap & (1 << (int) (s[i] - 'a'))) {
            return s[i];
        }
        bitmap = bitmap | (1 << (int) (s[i] - 'a'));
    }
    return s[0];
}