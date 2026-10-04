import contextlib
import io
import unittest

from binarybitops import (
    CloudResource,
    OnPremResource,
    SecureHybridEnvironment,
)


class EnvironmentTests(unittest.TestCase):
    def test_resource_locations_and_controls(self):
        local = OnPremResource("Git", "Source Control", ["MFA"])
        cloud = CloudResource("Kubernetes", "Runtime", ["RBAC"])
        self.assertEqual(local.location, "On-Premises")
        self.assertEqual(cloud.location, "Cloud")
        self.assertEqual(local.security_controls, ["MFA"])
        self.assertEqual(cloud.security_controls, ["RBAC"])

    def test_resource_lists_are_independent(self):
        first = CloudResource("First", "Runtime")
        second = CloudResource("Second", "Runtime")
        first.security_controls.append("TLS")
        self.assertEqual(second.security_controls, [])

    def test_empty_environment_warns(self):
        env = SecureHybridEnvironment()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            env.audit_security()
        self.assertIn("WARNING: No secure connectivity configured", output.getvalue())
        self.assertIn("WARNING: No security policies defined", output.getvalue())

    def test_display_includes_configured_resources_and_policies(self):
        env = SecureHybridEnvironment()
        env.add_onprem(OnPremResource("Git", "Source Control", ["MFA"]))
        env.add_cloud(CloudResource("Kubernetes", "Runtime", ["RBAC"]))
        env.add_connectivity("VPN")
        env.add_policy("Encryption")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            env.display()
        for expected in ("Git", "Kubernetes", "MFA", "RBAC", "VPN", "Encryption"):
            self.assertIn(expected, output.getvalue())


if __name__ == "__main__":
    unittest.main()
