class Person:
    def __init__(self, full_name, email, work_phone, org_name):
        self._full_name = full_name
        self._email = email
        self._work_phone = work_phone
        self._org_name = org_name

    # Overloading the greater than (>) operator
    def __gt__(self, other):
        """! Overriding the > operator.
        Comparison is first made by the `org_name` attribute, then by the `full_name` attribute, and finally by the `work_phone` attribute.

        @param other: Object to the right of the operator
        @return: True if self > other, False otherwise
        """
        # Check if the object to the right of the operator is of type `Person`
        if not isinstance(other, Person):
            raise TypeError("Only for Person objects")

        # Return the result of the comparison
        return not self.__le__(other)

    # Overloading the less than (<) operator
    def __lt__(self, other):
        """! Overriding the < operator.
        Comparison is first made by the `org_name` attribute, then by the `full_name` attribute, and finally by the `work_phone` attribute.

        @param other: Object to the right of the operator
        @return: True if self < other, False otherwise
        """
        # Check if the object to the right of the operator is of type `Person`
        if not isinstance(other, Person):
            raise TypeError("Only for Person objects")

        # Return the result of the comparison
        return not self.__ge__(other)

    # Overloading the greater than or equal to (>=) operator
    def __ge__(self, other):
        """! Overriding the >= operator.
        Comparison is first made by the `org_name` attribute, then by the `full_name` attribute, and finally by the `work_phone` attribute.

        @param other: Object to the right of the operator
        @return: True if self >= other, False otherwise
        """
        # Check if the object to the right of the operator is of type `Person`
        if not isinstance(other, Person):
            raise TypeError("Only for Person objects")

        # Compare the org_name attribute first
        if self.org_name == other.org_name:
            # If org_name is equal, compare the full_name attribute
            if self.full_name == other.full_name:
                # If both org_name and full_name are equal, compare the work_phone attribute
                return self.work_phone >= other.work_phone
            else:
                return self.full_name >= other.full_name
        else:
            return self.org_name >= other.org_name

    # Overloading the less than or equal to (<=) operator
    def __le__(self, other):
        """! Overriding the <= operator.
        Comparison is first made by the `org_name` attribute, then by the `full_name` attribute, and finally by the `work_phone` attribute.

        @param other: Object to the right of the operator
        @return: True if self <= other, False otherwise
        """
        # Check if the object to the right of the operator is of type `Person`
        if not isinstance(other, Person):
            raise TypeError("Only for Person objects")

        # Compare the org_name attribute first
        if self.org_name < other.org_name:
            return True
        elif self.org_name > other.org_name:
            return False
        else:
            # If org_name is equal, compare the full_name attribute
            if self.full_name < other.full_name:
                return True
            elif self.full_name > other.full_name:
                return False
            else:
                # If both org_name and full_name are equal, compare the work_phone attribute
                return self.work_phone <= other.work_phone

    # Overloading the equal to (==) operator
    def __eq__(self, other):
        """! Overriding the == operator.
        Comparison is made by comparing the values of all attributes of the `Person` object.

        @param other: Object to the right of the operator
        @return: True if all attributes are equal, False otherwise
        """
        # Check if the object to the right of the operator is of type `Person`
        if not isinstance(other, Person):
            raise TypeError("Only for Person objects")

        # Return the result of the comparison
        return (self.full_name == other.full_name and
                self.org_name == other.org_name and
                self.work_phone == other.work_phone and
                self.email == other.email)


    # Getters

    # Property for full_name
    @property
    def full_name(self):
        return self._full_name

    # Property for org_name
    @property
    def org_name(self):
        return self._org_name

    # Property for work_phone
    @property
    def work_phone(self):
        return self._work_phone

    # Property for email
    @property
    def email(self):
        return self._email