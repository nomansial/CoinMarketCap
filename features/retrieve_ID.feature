
  Feature: Backend Tasks

    @Test
    Scenario: Backend Task 1 Part 1 - Retrieve the IDs
      Given API KEY is provided
      When cryptocurrency map API is executed
      Then BTC USDT and ETH ID are retrieved

    @Test
    Scenario Outline: Backend Task 1 Part 2 - Convert Currency
      Given API KEY is provided
      When User provides <amount> and <currencyID> to covert to <secondCurrency>
      Then Currency is converted successfully
      Examples:
        | amount  | currencyID | secondCurrency |
        |  20     | 1          |  PAK           |

    @Test
    Scenario Outline: Backend Task 2 Part 1 - Retrieve the IDs
      Given API KEY is provided
      When cryptocurrency info API <ID> is provided
      Then response is received
      Examples:
      | ID    |
      | 1027  |
