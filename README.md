# Fast Api With GraphQL
![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7BEVXTJQwdfvUkJBNeZjLzfFUKKWFICnaOw&usqp=CAU)

### Introduction

Objective of this repo is to build graphql server with fast api and connecting it to mySQL database.

### GraphQL

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. The difference between Rest and GraphQL is that for RestAPi you need to define endpoint for each response, for example

RestAPI
1. Create `/users` endpoint to get user info
2. Create `/posts/{user_id}` endpoint to get posts by that user
3. Create `/comments/{post_id}/{user_id}` to get comments related to the post and user

And other endpoints based on the requirements

Where as GraphQL you can just build one endpoint and describe the attributes just like a SQL query and get the response, and in the same endpoint you can get users, post and comments data for that user, example below:

![firstImg](https://i.ibb.co/Wz2Yg4V/Screenshot-2020-11-24-at-12-57-19-PM.png)


### Fast API

Amazing python lib for building API and even web apps check it out here [FastAPI](https://fastapi.tiangolo.com)

### How to run
1. Clone this repo
2. Create new env e.g `conda create --name gfastpy37`
3. Run `pip install -r requirements.txt`
4. Run `uvicorn main:app --reload`
5. Open `127.0.0.1:8000/graphql`

### Sample queries

```
mutation createUser {
  createUser(userDetails: {name: "Fadil", address: "Somewhere on earth", phoneNumber: "0193888583", sex: "male"}) {
    id
    name
    address
    phoneNumber
    sex
    posts {
      body
      comments {
        body
      }
    }
  }
}

mutation createPost {
  createPost(postDetails: {userId: 1, title: "My first blog", body: "This is a blog about myself"}) {
    id
    title
    body
  }
}

mutation createComment {
  createComment(commentDetails: {
    userId: 1, 
    postId: 1, 
    body: "Graphql looks interesting"
  }) {
    id
    postId
    body
  }
}

query getAllUsers {
  listUsers {
    id
    name
    address
    sex
    posts {
      title
      body
      comments {
        body
      }
    }
  }
}

query getUser {
  getSingleUser(userId: 1) {
    id
    name
    address
    phoneNumber
    sex
    posts{
      title
      body
    }
    comments {
      body
    }
  }
}

query getUserOnly {
  getSingleUser(userId: 422) {
    name
  }
}

```

### Kudos!
