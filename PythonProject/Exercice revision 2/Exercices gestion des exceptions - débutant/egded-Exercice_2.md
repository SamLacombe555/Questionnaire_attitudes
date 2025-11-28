# Tableau de tests – exceptions `permuter_elements_liste`

| Cas de test (liste, i, j) | Exception attendue | Raison |
|---------------------------|--------------------|--------|
| `([], 0, 1)`              |                    |        |
| `([1,2,3], 5, 1)`         |                    |        |
| `([1,2,3], -5, 1)`        |                    |        |
| `(None, 0, 1)`            |                    |        |
| `(123, 0, 1)`             |                    |        |
| `("abc", 0, 2)`           |                    |        |