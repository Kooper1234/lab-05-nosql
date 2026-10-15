// Step 2: use bookstore
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
printjson(db.authors.find().toArray())
printjson(db.books.find().toArray())

// Step 6: insert two new books
db.books.insertMany([
  { title: "The Long Earth", published_year: 2012, author_ids: ["author_003", "author_004"] },
  { title: "Frankenstein", published_year: 1818, author_ids: ["author_005"] }
])

// Step 7: add missing authors
db.authors.insertMany([
  {
    _id: "author_004",
    name: "Stephen Baxter",
    nationality: "British",
    bio: {
      short: "British science fiction author.",
      long: "Stephen Baxter is a British author of hard science fiction. He co-wrote The Long Earth with Terry Pratchett."
    }
  },
  {
    _id: "author_005",
    name: "Mary Shelley",
    nationality: "British",
    bio: {
      short: "British novelist who wrote Frankenstein.",
      long: "Mary Shelley was a British novelist. Her 1818 novel Frankenstein is often called the first science fiction novel."
    }
  }
])

// Step 8: filter books by a list of authors
printjson(db.books.find({ author_ids: { $in: ["author_001", "author_004"] } }).toArray())