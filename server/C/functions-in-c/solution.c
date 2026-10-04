
    if (b > max)
        max = b;

    if (c > max)
        max = c;

    if (d > max)
        max = d;

    return max;
}

int main() {
    int a, b, c, d;

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);

    printf("%d", max_of_four(a, b, c, d));

    return 0;
}