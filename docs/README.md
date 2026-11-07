# DriveStat Requirements

## User Stories

1. As an **administrator**, I want to **create and moderate accounts and the database** so I can **keep track of the users and add/remove any data**.

   * **Acceptance Criteria:** An admin panel should exist, in which accounts can be viewed, created and moderated, including the user data in the database.
2. As a **vehicle user**, I want to **enter my refueling/charging sessions** so I can **keep track of my fuel/energy consuption**.

   * **Acceptance Criteria:** A refueling panel should exist, in which users can enter their refueling sessions.
   * **Acceptance Criteria:** The fuel/energy data should be visible on the user web page.
3. As a **vehicle user**, I want to **connect my vehicle trip data to the database** so I can **keep track of my trips**.

   * **Acceptance Criteria:** A user should be able to connect their vehicle to the database which uploads the trip details after every ride, provided the inputs are positive.
   * **Acceptance Criteria:**The trip data should be visible on the user web page.
4. As a **vehicle user**, I want to **estimate fuel/energy cost when I enter a driven distance** so I can **calculate how much a trip costs**.

   * **Acceptance Criteria:** A panel with a trip cost calculator should exist, in which a user can enter their driven distance to estimate the cost of fuel/energy of a trip.
5. As a **vehicle user**, I want to **view my monthly statistics** so I can **see how far I drove and how much that cost this month**.

   * **Acceptance Criteria:** A panel with a monthly vehicle overview should exist, in which a user can see the driven distance, average fuel consumption and refueling/energy cost.
6. As a **vehicle user**, I want to **edit erroneous refueling/energy data** so I can **correct typos and other errors**.

   * **Acceptance Criteria:** In the refueling/energy data list, a user should be able to edit data they posted.

## Mis-user Stories

1. As a **malicious user**, I want to **make malicious sql commands** so I can **edit or read the database**.

   * **Mitigation Criteria:** Only accept parameterized api requests so no sql injection can happen.
2. As a **unauthorized user**, I want to **be able to make an account** so I can **use the advantages of DriveStat**.

   * **Mitigation Criteria:** Only the administrator should be able to create accounts, so they can keep track of who uses DriveStat.
3. As a **malicious hacker**, I want to **break into the DriveStat API** so I can **take control of the complete server**.

   * **Mitigation Criteria:** The API should run in a dockerized environment, so it is impossible to break out of the environment.
4. As a **malicious hacker**, I want to **be able to access the /admin part of the website** so I can **bruteforce my way into the admin console**.

   * **Mitigation Criteria:** Require two-factor authentication to log into the admin console.
   * **Mitigation Criteria:** The /admin part should only be visible on the local network, and nowhere else.



## Mockup



!\[Admin Mockup](./Images/AdminMockup.png)

!\[User Mockup](./Images/UserMockup.png)

!\[Database Mockup](./Images/DatabaseMockup.png)



