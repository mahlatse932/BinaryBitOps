class Resource:
    def __init__(self, name, category, location, security_controls=None):
        self.name = name
        self.category = category
        self.location = location
        self.security_controls = security_controls or []

    def describe(self):
        print(f"- {self.name} ({self.category}) in {self.location}")
        if self.security_controls:
            print(f"  Security: {', '.join(self.security_controls)}")


class OnPremResource(Resource):
    def __init__(self, name, category, security_controls=None):
        super().__init__(name, category, location="On-Premises", security_controls=security_controls)


class CloudResource(Resource):
    def __init__(self, name, category, security_controls=None):
        super().__init__(name, category, location="Cloud", security_controls=security_controls)


class SecureHybridEnvironment:
    def __init__(self):
        self.onprem_resources = []
        self.cloud_resources = []
        self.connectivity = []
        self.policies = []

    def add_onprem(self, resource):
        self.onprem_resources.append(resource)

    def add_cloud(self, resource):
        self.cloud_resources.append(resource)

    def add_connectivity(self, description):
        self.connectivity.append(description)

    def add_policy(self, policy):
        self.policies.append(policy)

    def display(self):
        print("=== Secure Hybrid Development Environment ===")
        print("\nOn-Premises Resources:")
        for resource in self.onprem_resources:
            resource.describe()

        print("\nCloud Resources:")
        for resource in self.cloud_resources:
            resource.describe()

        print("\nSecure Connectivity:")
        for item in self.connectivity:
            print(f"- {item}")

        print("\nSecurity Policies and Controls:")
        for policy in self.policies:
            print(f"- {policy}")

    def audit_security(self):
        print("\n=== Security Audit Summary ===")
        if not self.connectivity:
            print("WARNING: No secure connectivity configured")
        if not self.policies:
            print("WARNING: No security policies defined")
        else:
            print("All required security controls are present in the environment model.")


if __name__ == "__main__":
    env = SecureHybridEnvironment()

    env.add_onprem(OnPremResource(
        name="GitLab Server",
        category="Source Control",
        security_controls=["MFA", "Network Firewall", "TLS"]
    ))
    env.add_onprem(OnPremResource(
        name="Jenkins Server",
        category="CI/CD",
        security_controls=["RBAC", "Dedicated Build Network"]
    ))
    env.add_onprem(OnPremResource(
        name="SonarQube Server",
        category="Code Quality",
        security_controls=["Encrypted Database", "Access Logging"]
    ))

    env.add_cloud(CloudResource(
        name="Kubernetes Cluster",
        category="Runtime",
        security_controls=["Network Policies", "Pod Security Standards", "Managed IAM"]
    ))
    env.add_cloud(CloudResource(
        name="Cloud Storage",
        category="Artifact Storage",
        security_controls=["Encryption at Rest", "Versioning", "Access Controls"]
    ))
    env.add_cloud(CloudResource(
        name="Secrets Management",
        category="Secret Store",
        security_controls=["Hardware-backed KMS", "Strict Access Policies"]
    ))

    env.add_connectivity("Secure VPN / ExpressRoute between on-premises and cloud")
    env.add_connectivity("Zero Trust network segmentation and micro-segmentation")

    env.add_policy("Identity federation with SSO and MFA")
    env.add_policy("Immutable infrastructure pipelines and artifact signing")
    env.add_policy("Centralized logging, monitoring, and alerting")
    env.add_policy("Data protection with encryption in transit and at rest")

    env.display()
    env.audit_security()