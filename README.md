# smash gg only

This contains code for grabbing info from smash gg. The goal is to have a list
of matches.

For example, given three players, A, B, and C,


```
A B
B C
C A
```

would be a potential list of matches.

## Discord Help

I asked for help about the query on 11/29/20, and I got these messages on 12/02/20:

<img src="https://i.imgur.com/mkHldQ1.png" alt="Discord Help 1">

<img src="https://i.imgur.com/E4JbSpN.png" alt="Discord Help 2">

His queries pasted here for clarity:

```graphql
query GetEventIDs($slug: String) {
  tournament(slug: $slug) {
    events {
      name
      id
    }
  }
}
```

```graphql
{
  "slug": "the-big-house-online"
}
```
