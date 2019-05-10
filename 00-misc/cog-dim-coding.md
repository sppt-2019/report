# Cognitive Dimensions Coding
## Not programming, but coding of statements
---

In the social sciences the term coding means roughly the same as tagging or annotating some material, typically interview transcriptions. In this file coding is used as the social science term. Statements are sentences, or time stamps, in the transcribed material that signify an instance where something relevant occurs.

### Total

| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | | |
| Closeness of Mapping    | | |
| Consistency             | | |
| Diffuseness/Terseness   | | |
| Error-proneness         | | |
| Hard Mental Operations  | | |
| Hidden Dependencies     | | |
| Premature Commitment    | | |
| Progressive Evaluation  | | |
| Role-expressiveness     | | |
| Secondary Notation and Escape from Formalism | | |
| Viscosity               | | |
| Visibility and Juxtaposability | | |

### Participant 1

% 09:11 consistency affords participant understanding
% Extensive use of Secondary Notation and Escape from Formalism
| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | | |
| Closeness of Mapping    | | |
| Consistency             | | ff |
| Diffuseness/Terseness   | | f c |
| Error-proneness         | | f |
| Hard Mental Operations  | | |
| Hidden Dependencies     | | f c |
| Premature Commitment    | | f |
| Progressive Evaluation  | | ff |
| Role-expressiveness     | | f c |
| Secondary Notation and Escape from Formalism | | |
| Viscosity               | | |
| Visibility and Juxtaposability | | |

### Participant 2

| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | | |
| Closeness of Mapping    | | |
| Consistency             | | f c | <!-- Unity methods: translate --> <!-- reference type confusion -->
| Diffuseness/Terseness   | | f (c) | <!-- lambda expressions --> <!-- multiple foreach -->
| Error-proneness         | | ff | <!-- closures and parameters/arguments -->
| Hard Mental Operations  | | ff cc | <!-- List operations, lambda expressions --> <!-- List operations, concurrency and synchronisation -->
| Hidden Dependencies     | | f | <!-- Unity SerialisedField -->
| Premature Commitment    | | f | <!-- let before member -->
| Progressive Evaluation  | | c | <!-- unnecessary ref keyword not highlighted -->
| Role-expressiveness     | | |
| Secondary Notation and Escape from Formalism | | |
| Viscosity               | | | <!-- Poor design results in high viscosity in C# -->
| Visibility and Juxtaposability | | |

### Participant 3

| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | | |
| Closeness of Mapping    | | |
| Consistency             | | f | <!-- Implicit return -->
| Diffuseness/Terseness   | | |
| Error-proneness         | | ff | <!-- Strong Types and array != list -->
| Hard Mental Operations  | | |
| Hidden Dependencies     | | |
| Premature Commitment    | | |
| Progressive Evaluation  | | |
| Role-expressiveness     | | f | <!-- List.sum -->
| Secondary Notation and Escape from Formalism | | |
| Viscosity               | | |
| Visibility and Juxtaposability | | |
<!-- Good use of modularity -->

### Participant 4

| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | F? (participant does not understand function abstraction) | |
| Closeness of Mapping    | F (participant states that he does not know what ReactTo means)  | |
| Consistency             | F (participant does not realise that F# is indent based) F (participant wants to use += in assignment instead of <-) F (participant does not associate ReactTo generic types with the input parameter to filter and handler) C (participant forgets a ;) | |
| Diffuseness/Terseness   | F (participant is not sure what the arrows in lambda expressions mean) F (parantheses are hard, they look like bananas) | |
| Error-proneness         | F (participant forgets .0 in float) F (participant uses incorrect indentation in lambda expressions) F (participant ends a funciton with a boolean expression instead of an assignment) C (participant adds a Vector3 field on the class, which could easily have been a local in Update) | |
| Hard Mental Operations  | F (participant has a hard time matching pairs of brackets) | |
| Hidden Dependencies     | | |
| Premature Commitment    | | |
| Progressive Evaluation  | F (participant implements a single direction and attempts to evaluate in Unity) | |
| Role-expressiveness     | F (participant does not wish to use MoveAxis, but uses KeyCode-filtered Keyboard instead) F (participant is confused with the tuple operator and multiplication) F (Participants attempt to call an enum as a function) | |
| Secondary Notation and Escape from Formalism | C (participant decides to group Unity-assigned fields and code-assigned fields) | |
| Viscosity               | C (participant attempts to implement strafing and in the process unintentionally deletes the jumping functionality) | |
| Visibility and Juxtaposability | F (participant opens documentation and IDE side-by-side) C (participant pulls up the documentation of RotateAround before applying it) | |

He likes C# because the code is allowed to "jump around". He arbitrarily tries inserting and removing indents when errors occur.

He does not prioritise learning new stuff because "things are already working". Participant does not know what a tuple is.

He is unsure how to write lambdas with multiple statements and is confused by what 'fun m ->' means in the documentation.

Validity issue: The move mouse example is jibberish and it is not clearly indicated that the code may only be used for the structure. The documentation lacks a description and the participant asks if v and h are mouse coordinates or movement.

Validity issue (C#): Participant asks if he should do it rapidly or nicely, to which the facilitator answers nicely.

Participant mentions that he would always prefer buying player controllers as their notoriously hard to implement. This is echoed by many other participant.

Participant still uses Unity 5!?

Participant notices that RotateAround is deprecated and switches to Rotate, while noting that he hopes that it has become one of its overloads.

F (participant attempts to implement a type to move FRPBehaviour forward) F (participant wants to accumulate all input in a Vector3, which is applied as the last step in Update)

### Participant 6

| Attention Investment Metric | Code Frequency | Dot |
|:---                     |:--:|:--:|
| Abstract Gradient       | C (participant chooses to copy-paste 4 lines of code instead of implementing a function) | |
| Closeness of Mapping    | (F (participant does not want to use types because it's functional)) | |
| Consistency             | F (participant is unsure when to use <- and =) F (participant is inconsistent in the use of explicit types) F (participant is unsure how to iterate a list) F (participant forgets the 'fun' keyword when defining a lambda) F (Participant tries several times to do namebindings without assignment.) | |
| Diffuseness/Terseness   | | |
| Error-proneness         | F (Participant forgets 'let' several times in both functions and name bindings) F (Participant forgets the . before []) F (implicit return, twice even after being told) C (Participant copy pastes function arguments into algebraic expression and mixes up the order) | |
| Hard Mental Operations  | F (participant is struggling with iterating or recursing through the collection) C? (participant has a hard time expressing algebra) | |
| Hidden Dependencies     | | |
| Premature Commitment    | F (Participant defines a 'let' function after the 'member's) | |
| Progressive Evaluation  | F (participant attempts to write pseudo code to remove errors) C (compiler complains about the use of uninitialised variables) | |
| Role-expressiveness     | F (unit) F (participant does not know that constructors are the parantheses after type) C (participant manually enforces order of evaluation by inserting parantheses) | |
| Secondary Notation and Escape from Formalism | C (participant uses blocking to logically order the expressions in correct and incorrect) | |
| Viscosity               | F (participant has chosen to use explicit types) | |
| Visibility and Juxtaposability | F (Participant pulls up the documentation of List.iter and List.find) F (Participant attempts to pull up the documentation for the Node class) | |

Task formulation: Participant believes that he is to construct a F# type that contains the Node-class, causing the task to become unnecessarily hard.

Participant states that he is jumping between different ways of doing things.

Eventhough the tasks were designed to be implemented with map-reduce, the participant does not use it at all.

Participant notes that he thinks it's faster when he is allowed to use variables ~ 54:00 circa
