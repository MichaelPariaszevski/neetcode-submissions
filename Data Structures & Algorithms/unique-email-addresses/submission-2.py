class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result_set: Set[Tuple(str, str)] = set()

        for email in emails: 
            split_email = email.split("@")
            local_name = split_email[0]
            domain_name = split_email[1]
            local_name = local_name.replace(".", "")
            local_found = local_name.find("+")
            if local_found != -1: 
                local_name = local_name[:local_found]

            result_set.add((local_name, domain_name))

        return len(result_set)




        