## New Feature Update: Split System

We've added a new "Split system" feature to the program. Now, users can use our slashbot to log expenses for multiple members, recording the exact amount and item of each person's expenditure. Simultaneously, this new feature allows the specification of debtors and payers, taking into account that during group spending activities, some might pay on behalf of others.

Suppose there's a group spending scenario. Calculating how much each person should transfer to others can be a complicated process. Our new feature addresses this challenge perfectly. By inputting each person's actual expenditure and payments, you can swiftly determine how much each member should collect or pay to others. We believe that this new functionality greatly expands slashbot's use-cases, transitioning it from a purely personal application to one suitable for group scenarios.

## Inspiration for the New Feature:

The inspiration came from an outing with our team members. During the trip, some members did not carry their credit cards, lacking feasible payment methods, so others in the group covered their expenses. By the end of the day, when we gathered to calculate the day's expenses, we found the process of splitting the bill to be somewhat cumbersome. This experience led us to wonder: why not add a new feature to slashbot to address this issue? Hence, the Split System was born.

## Feature Demonstration Video

A video link showcases our newly released feature. Just like the previous slashbot, it interacts with users via an API connection to Telegram.

## Technical Challenges Addressed During Development:

### The codebase lacked comprehensive documentation. 
There were a few comments here and there, but they didn't provide a clear understanding of the code's overall structure and logic. Especially, there are no comments on what is the purpose of each variable used and the code was complex, with long functions and nested conditional statements. The original developers who wrote the legacy code may have left the project. As a result, there may be limited knowledge transfer about the code's intricacies and design decisions, further complicating the task of understanding and modifying it.

So, we had to spend extra time reading through the code and making notes to create our own url and sequence diagram. Besides, we started an internal knowledge-sharing initiative where team members document their understanding of complex sections of the codebase.

Moreover, We had to be cautious about making changes because modifying one part of the code could inadvertently affect other parts. To mitigate this risk, we conducted comprehensive tests after each change to ensure we didn't introduce new issues.




## Development Team Communication:

We primarily communicate through our Discord group. Here's the link to our Discord group: [https://discord.gg/thZvPQwr](https://discord.gg/thZvPQwr)
