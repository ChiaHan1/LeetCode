char repeatedCharacter(char* s) {
    uint32_t bitmap = 0;
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        int key = 1 << (int) (s[i] - 'a');
        if (bitmap & key) {
            return s[i];
        }
        bitmap = bitmap | key;
    }
    return s[0];
}