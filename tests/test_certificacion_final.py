"""
🎯 TEST FINAL DEFINITIVO - AI FACTORY
=====================================

Test completamente optimizado que maneja todos los edge cases correctamente
y proporciona un veredicto final preciso para publicación.

OBJETIVO: Certificación 100% confiable para PyPI/GitHub
"""

import requests
import json
import time
import subprocess
import os
from typing import Dict, List, Any
from datetime import datetime


class AIFactoryFinalTester:
    """Tester final definitivo para certificación de AI Factory"""
    
    def __init__(self, base_url: str = "http://127.0.0.1:8010"):
        self.base_url = base_url
        self.test_results = []
        self.critical_failures = []
        self.minor_issues = []
        self.passed_tests = []
        self.test_model_name = f"final-test-{int(time.time())}"
        
    def log_result(self, test_name: str, status: str, severity: str, details: str = ""):
        """Registra resultado con clasificación de severidad"""
        result = {
            "test": test_name,
            "status": status,
            "severity": severity,  # "critical", "minor", "pass"
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        
        self.test_results.append(result)
        
        if status == "✅ PASS":
            self.passed_tests.append(result)
            print(f"✅ {test_name}: {details}")
        elif severity == "critical":
            self.critical_failures.append(result)
            print(f"🚨 {test_name}: {details} (CRITICAL)")
        elif severity == "minor":
            self.minor_issues.append(result)
            print(f"⚠️ {test_name}: {details} (MINOR)")
        else:
            print(f"❌ {test_name}: {details}")
    
    def safe_api_call(self, method: str, endpoint: str, data: Dict = None, 
                     expected_status: List[int] = [200], test_name: str = None,
                     severity: str = "critical") -> Dict:
        """API call seguro con clasificación de severidad"""
        try:
            url = f"{self.base_url}{endpoint}"
            
            if method.upper() == "GET":
                response = requests.get(url, timeout=30)
            elif method.upper() == "POST":
                response = requests.post(url, json=data, timeout=30)
            elif method.upper() == "DELETE":
                response = requests.delete(url, timeout=30)
            
            if response.status_code in expected_status:
                try:
                    json_data = response.json()
                except:
                    json_data = {"response": response.text}
                
                self.log_result(test_name, "✅ PASS", "pass", f"Status {response.status_code}")
                return {"success": True, "data": json_data, "status": response.status_code}
            else:
                self.log_result(test_name, "❌ FAIL", severity, 
                              f"Expected {expected_status}, got {response.status_code}")
                return {"success": False, "error": response.text, "status": response.status_code}
                
        except Exception as e:
            self.log_result(test_name, "❌ FAIL", severity, f"Exception: {str(e)}")
            return {"success": False, "error": str(e)}

    def test_critical_api_core(self):
        """Tests críticos que DEBEN funcionar para publicación"""
        print("\n🚨 === TESTS CRÍTICOS - API CORE ===")
        
        # Estos son absolutamente críticos
        self.safe_api_call("GET", "/health", test_name="CRITICAL - Health Check", severity="critical")
        self.safe_api_call("GET", "/models", test_name="CRITICAL - List Models", severity="critical")
        
    def test_critical_model_management(self):
        """Tests críticos de gestión de modelos"""
        print("\n🤖 === TESTS CRÍTICOS - MODEL MANAGEMENT ===")
        
        # Crear modelo - crítico
        create_data = {
            "model_name": self.test_model_name,
            "base_prompt": "Eres un asistente de testing final.",
            "version": "1.0"
        }
        result = self.safe_api_call("POST", "/models/create", create_data, 
                                  test_name="CRITICAL - Create Model", severity="critical")
        
        if result["success"]:
            # Obtener detalles - crítico
            self.safe_api_call("GET", f"/models/{self.test_model_name}", 
                             test_name="CRITICAL - Get Model Details", severity="critical")
            
            # Añadir prompt - importante pero no crítico
            add_data = {
                "model_name": self.test_model_name,
                "new_prompt": "Prompt adicional para testing.",
                "examples": [{"input": "test", "output": "response"}]
            }
            self.safe_api_call("POST", "/models/add_prompt", add_data, 
                             test_name="Add Prompt", severity="minor")
    
    def test_star_feature_comparison(self):
        """Test de la funcionalidad estrella - CRÍTICO"""
        print("\n⭐ === TEST CRÍTICO - FUNCIONALIDAD ESTRELLA ===")
        
        # Usar modelo existente con versiones
        existing_model = "modelo-comparacion-test"
        
        # Compare versions - ABSOLUTAMENTE CRÍTICO
        result = self.safe_api_call("GET", f"/models/{existing_model}/compare", 
                                  test_name="CRITICAL - Compare Versions (STAR FEATURE)", 
                                  severity="critical")
        
        if result["success"]:
            data = result["data"]
            
            # Verificar algoritmo de recomendación - CRÍTICO
            if "recommendation" in data and "best_version" in data["recommendation"]:
                self.log_result("CRITICAL - Recommendation Algorithm", "✅ PASS", "pass", 
                              "Star feature algorithm working")
                
                # Verificar confianza
                confidence = data["recommendation"].get("confidence", 0)
                if isinstance(confidence, (int, float)) and 0 <= confidence <= 1:
                    self.log_result("Confidence Score Validation", "✅ PASS", "pass", 
                                  f"Valid confidence: {confidence}")
                else:
                    self.log_result("Confidence Score Validation", "❌ FAIL", "minor", 
                                  f"Invalid confidence: {confidence}")
            else:
                self.log_result("CRITICAL - Recommendation Algorithm", "❌ FAIL", "critical", 
                              "Star feature algorithm BROKEN")
        
        # Deploy info - importante
        self.safe_api_call("GET", f"/models/{existing_model}/deploy-info", 
                         test_name="Deploy Info", severity="minor")
    
    def test_deployment_system(self):
        """Test del sistema de deployment - importante"""
        print("\n🚀 === TEST DEPLOYMENT SYSTEM ===")
        
        deploy_data = {
            "model_name": "modelo-comparacion-test",
            "version": "1.0.1"
        }
        
        result = self.safe_api_call("POST", "/models/deploy", deploy_data, 
                                  test_name="Deploy Model", severity="minor")
        
        if result["success"] and "deployment_folder" in result["data"]:
            self.log_result("Deploy Package Generation", "✅ PASS", "pass", 
                          "Deploy system working")
    
    def test_cli_functionality(self):
        """Test CLI - importante pero no crítico para API"""
        print("\n⌨️ === TEST CLI FUNCTIONALITY ===")
        
        # Test desde directorio correcto
        try:
            result = subprocess.run(["python", "-m", "ai_factory.cli", "check"], 
                                  capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                self.log_result("CLI Check Command", "✅ PASS", "pass", "CLI working correctly")
                
                # Si check funciona, probar info
                result2 = subprocess.run(["python", "-m", "ai_factory.cli", "info"], 
                                       capture_output=True, text=True, timeout=10)
                if result2.returncode == 0:
                    self.log_result("CLI Info Command", "✅ PASS", "pass", "CLI info working")
                else:
                    self.log_result("CLI Info Command", "❌ FAIL", "minor", "CLI info failed")
            else:
                self.log_result("CLI Check Command", "❌ FAIL", "minor", 
                              "CLI not working (not critical for API)")
                
        except Exception as e:
            self.log_result("CLI Functionality", "❌ FAIL", "minor", 
                          f"CLI test exception: {str(e)}")
    
    def test_performance_basic(self):
        """Test básico de performance"""
        print("\n⚡ === TEST PERFORMANCE ===")
        
        start_time = time.time()
        
        # 3 requests rápidos
        success_count = 0
        for i in range(3):
            result = self.safe_api_call("GET", "/health", 
                                      test_name=f"Performance Test {i+1}", severity="minor")
            if result["success"]:
                success_count += 1
        
        duration = time.time() - start_time
        
        if success_count == 3 and duration < 5:
            self.log_result("Performance Overall", "✅ PASS", "pass", 
                          f"3 requests in {duration:.2f}s")
        elif success_count == 3:
            self.log_result("Performance Overall", "⚠️ SLOW", "minor", 
                          f"3 requests in {duration:.2f}s (slow but working)")
        else:
            self.log_result("Performance Overall", "❌ FAIL", "minor", 
                          f"Only {success_count}/3 requests successful")
    
    def cleanup(self):
        """Limpieza final"""
        print("\n🧹 === CLEANUP ===")
        
        self.safe_api_call("DELETE", f"/models/{self.test_model_name}", 
                         expected_status=[200, 404], test_name="Cleanup", severity="minor")
    
    def run_final_certification(self):
        """Ejecuta certificación final completa"""
        print("🎯 INICIANDO CERTIFICACIÓN FINAL DE AI FACTORY")
        print("=" * 60)
        print("🎯 OBJETIVO: Determinar si está listo para PyPI/GitHub")
        print("=" * 60)
        
        start_time = datetime.now()
        
        try:
            # Tests en orden de criticidad
            self.test_critical_api_core()
            self.test_critical_model_management()
            self.test_star_feature_comparison()
            self.test_deployment_system()
            self.test_cli_functionality()
            self.test_performance_basic()
            self.cleanup()
            
        except Exception as e:
            self.log_result("Test Suite", "❌ FAIL", "critical", f"Test suite crashed: {str(e)}")
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        # Generar veredicto final
        return self.generate_final_verdict(duration)
    
    def generate_final_verdict(self, duration):
        """Genera veredicto final para certificación"""
        print("\n" + "=" * 60)
        print("🏆 CERTIFICACIÓN FINAL - AI FACTORY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed = len(self.passed_tests)
        critical_failed = len(self.critical_failures)
        minor_issues = len(self.minor_issues)
        
        print(f"⏱️ Duración: {duration}")
        print(f"🧪 Tests totales: {total_tests}")
        print(f"✅ Tests pasados: {passed}")
        print(f"🚨 Fallos críticos: {critical_failed}")
        print(f"⚠️ Issues menores: {minor_issues}")
        
        # Criterio de certificación
        if critical_failed == 0:
            if minor_issues == 0:
                verdict = "🌟 PERFECTO - PUBLICAR INMEDIATAMENTE"
                confidence = "100%"
                status = "APPROVED"
            elif minor_issues <= 2:
                verdict = "✅ EXCELENTE - LISTO PARA PUBLICACIÓN" 
                confidence = "95%"
                status = "APPROVED"
            else:
                verdict = "✅ BUENO - APTO PARA PUBLICACIÓN"
                confidence = "85%"
                status = "APPROVED"
        else:
            verdict = "❌ NO LISTO - FALLOS CRÍTICOS DETECTADOS"
            confidence = "0%"
            status = "REJECTED"
        
        print(f"\n🎯 VEREDICTO FINAL: {verdict}")
        print(f"📊 Confianza: {confidence}")
        
        # Mostrar fallos críticos si los hay
        if critical_failed > 0:
            print(f"\n🚨 FALLOS CRÍTICOS QUE BLOQUEAN PUBLICACIÓN:")
            for failure in self.critical_failures:
                print(f"   ❌ {failure['test']}: {failure['details']}")
        
        # Issues menores
        if minor_issues > 0:
            print(f"\n⚠️ ISSUES MENORES (no bloquean publicación):")
            for issue in self.minor_issues:
                print(f"   ⚠️ {issue['test']}: {issue['details']}")
        
        # Funcionalidades críticas verificadas
        print(f"\n✅ FUNCIONALIDADES CRÍTICAS VERIFICADAS:")
        
        health_ok = any("Health Check" in t["test"] and t["status"] == "✅ PASS" for t in self.test_results)
        models_ok = any("List Models" in t["test"] and t["status"] == "✅ PASS" for t in self.test_results)
        create_ok = any("Create Model" in t["test"] and t["status"] == "✅ PASS" for t in self.test_results)
        star_ok = any("Compare Versions" in t["test"] and t["status"] == "✅ PASS" for t in self.test_results)
        algo_ok = any("Recommendation Algorithm" in t["test"] and t["status"] == "✅ PASS" for t in self.test_results)
        
        print(f"   🏥 API Health: {'✅' if health_ok else '❌'}")
        print(f"   📋 Model Listing: {'✅' if models_ok else '❌'}")
        print(f"   🤖 Model Creation: {'✅' if create_ok else '❌'}")
        print(f"   ⭐ Version Comparison: {'✅' if star_ok else '❌'} (FUNCIONALIDAD ESTRELLA)")
        print(f"   🧠 Recommendation Algorithm: {'✅' if algo_ok else '❌'} (CORE VALUE)")
        
        if critical_failed == 0:
            print(f"\n🎉 ¡AI FACTORY ESTÁ CERTIFICADO PARA PUBLICACIÓN! 🎉")
            print(f"👍 Todas las funcionalidades críticas operativas")
            print(f"⭐ Funcionalidad estrella funcionando perfectamente")
            print(f"🚀 Listo para PyPI y GitHub")
        
        return {
            "status": status,
            "verdict": verdict,
            "confidence": confidence,
            "critical_failures": critical_failed,
            "minor_issues": minor_issues,
            "total_tests": total_tests,
            "passed": passed,
            "duration": str(duration),
            "ready_for_publication": critical_failed == 0
        }


def main():
    """Certificación final main"""
    print("🎯 AI FACTORY - CERTIFICACIÓN FINAL PARA PUBLICACIÓN")
    print("Verificando servidor...")
    
    try:
        response = requests.get("http://127.0.0.1:8010/health", timeout=5)
        if response.status_code == 200:
            print("✅ Servidor activo")
        else:
            print("❌ Servidor no responde")
            return
    except:
        print("❌ No se puede conectar al servidor")
        return
    
    # Ejecutar certificación
    tester = AIFactoryFinalTester()
    results = tester.run_final_certification()
    
    return results


if __name__ == "__main__":
    main()